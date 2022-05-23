# Copyright 2021 - 2022 German Cancer Research Center (DKFZ)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""module for job dao"""

import json
from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy import create_engine, insert, select, update

from exec_manager.dao.db_models import DBJob, metadata
from exec_manager.exec_profiles import ExecProfile, ExecProfileType
from exec_manager.jobs import Job, JobStatusType, PythonJob
from exec_manager.utils import WfLangType


class JobDAO(ABC):
    """abstract class for job dao"""

    @abstractmethod
    def create(
        self,
        job_status: JobStatusType,
        exec_profile: ExecProfile,
        workflow: dict,
        inputs: dict,
    ) -> UUID:
        """
        Inserts a job into the database.

        Parameters
        ----------
        job_status: JobStatusType
            current status of the job; initially it is JobStatusType.NOTSTARTED
        exec_profile: ExecProfile
            exec profile of this job
        workflow
            the jobs workflow
        inputs: dict
            the input parameters of the job

        Returns
        -------
        UUID
        """
        ...

    @abstractmethod
    def get(self, job_id: UUID) -> Job:
        """
        Returns a job by his job id.

        Parameters
        ----------
        job_id: UUID
            id of the job

        Returns
        -------
        Job
        """
        ...

    @abstractmethod
    def update(self, job_id: UUID, job: Job) -> None:
        """
        Updates a jobs by his id.

        Parameters
        ----------
        job_id: UUID
            id of the job
        job: Job
            updated job

        Returns
        -------
        None
        """
        ...


class SQLJobDAO(JobDAO):
    """class for sql job dao"""

    def __init__(self, db_url: str):
        """Initialize DB."""
        self._engine = create_engine(db_url)
        metadata.create_all(self._engine)

    def create(
        self,
        job_status: JobStatusType,
        exec_profile: ExecProfile,
        workflow: dict,
        inputs: dict,
    ) -> UUID:
        """
        Inserts a job into the database.

        Parameters
        ----------
        job_status: JobStatusType
            current status of the job; initially it is JobStatusType.NOTSTARTED
        exec_profile: ExecProfile
            exec profile of this job
        workflow: dict
            the jobs workflow
        inputs: dict
            the input parameters of the job

        Returns
        -------
        UUID
        """
        with self._engine.connect() as connection:
            cursor = connection.execute(
                insert(DBJob.__table__)
                .values(
                    job_status=job_status.value,
                    exec_profile=exec_profile.dict(),
                    workflow=workflow,
                    inputs=inputs,
                )
                .returning(DBJob.job_id)
            )
            result = cursor.fetchall
        return result[0][0]  # job_id

    def get(self, job_id: UUID) -> Job:
        """
        Returns a job by his job id.

        Parameters
        ----------
        job_id: UUID
            id of the job

        Returns
        -------
        Job
        """
        with self._engine.connect() as connection:
            cursor = connection.execute(
                select([DBJob.job_id, DBJob.job_status, DBJob.exec_profile]).where(
                    DBJob.job_id == str(job_id)
                )
            )
            result = cursor.fetchall()
            job_status = JobStatusType(result[0][1])
            exec_profile = json.loads(result[0][2])
            exec_profile = ExecProfile(
                type_=ExecProfileType(exec_profile["exec_profile_type"]),
                wf_lang=WfLangType(exec_profile["wf_lang"]),
            )
            inputs = json.loads(result[0][4])
            if exec_profile.type_ == ExecProfileType.PYTHON:
                return PythonJob(job_id, job_status, exec_profile, inputs)
            if exec_profile.type_ == ExecProfileType.BASH:
                raise NotImplementedError(
                    "Execution profiles of type Bash not supported, yet"
                )
            raise NotImplementedError(
                "Execution profiles of type WES not supported, yet"
            )

    def update(self, job_id: UUID, job: Job) -> None:
        """
        Updates a jobs by his id.

        Parameters
        ----------
        job_id: UUID
            id of the job
        job: Job
            updated job

        Returns
        -------
        None
        """
        with self._engine.connect() as connection:
            connection.execute(
                update(DBJob.__table__)
                .where(DBJob.job_id == str(job_id))
                .values(
                    job_status=job.job_status.value,
                    exec_profile=job.exec_profile.dict(),
                )
            )
