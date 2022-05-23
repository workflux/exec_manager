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

from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy import create_engine, insert, select, update

from exec_manager.dao.db_models import DBJob, metadata
from exec_manager.exec_profiles import ExecProfile, ExecProfileType
from exec_manager.jobs import Job, JobStatusType, PythonJob
from exec_manager.utils import WfLangType


class JobDAO(ABC):
    """abstract class for job dao

    Methods:
        create (UUID): inserts a job into database
        get (Job): returns a job by its id
        update (): updates a job by its id
    """

    @abstractmethod
    def create(
        self,
        job_status: JobStatusType,
        exec_profile: ExecProfile,
        workflow: dict,
        inputs: dict,
    ) -> UUID:
        """Inserts a job into the database.

        Args:
            job_status (JobStatusType): current status of the job;
                initially it is JobStatusType.NOTSTARTED
            exec_profile (ExecProfile): exec profile of this job
            workflow (dict): the jobs workflow
            inputs (dict): the input parameters of the job

        Returns:
            UUID: job id
        """
        ...

    @abstractmethod
    def get(self, job_id: UUID) -> Job:
        """Returns a job by its job id.

        Args:
            job_id (UUID): id of the job

        Returns:
            Job: job belongig to job id
        """
        ...

    @abstractmethod
    def update(self, job_id: UUID, job: Job) -> None:
        """Updates a jobs by its id.

        Args:
            job_id (UUID): id of the job
            job (Job): updated job
        """
        ...


class SQLJobDAO(JobDAO):
    """class for sql job dao

    Methods:
        create (UUID): inserts a job into database
        get (Job): returns a job by its id
        update (): updates a job by its id
    """

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
        """Inserts a job into the database.

        Args:
            job_status (JobStatusType): current status of the job;
                initially it is JobStatusType.NOTSTARTED
            exec_profile (ExecProfile): exec profile of this job
            workflow (dict): the jobs workflow
            inputs (dict): the input parameters of the job

        Returns:
            UUID: job id
        """
        with self._engine.connect() as connection:
            cursor = connection.execute(
                insert(DBJob.__table__).values(
                    job_status=job_status.value,
                    exec_profile={
                        "exec_profile_type": exec_profile.type_.value,
                        "wf_lang_type": exec_profile.wf_lang.value,
                    },
                    workflow=workflow,
                    inputs=inputs,
                )
            )
            job_id = cursor.inserted_primary_key[0]
        return job_id

    def get(self, job_id: UUID) -> Job:
        """Returns a job by its job id.

        Args:
            job_id (UUID): id of the job

        Raises:
            NotImplementedError: Bash exec profile is not implemented yet
            NotImplementedError: WES exec profile is not implemented yet

        Returns:
            Job: job belonging to job_id
        """
        with self._engine.connect() as connection:
            cursor = connection.execute(
                select([DBJob.job_id, DBJob.job_status, DBJob.exec_profile]).where(
                    DBJob.job_id == str(job_id)
                )
            )
            result = cursor.fetchall()
            job_status = JobStatusType(result[0][1])
            exec_profile = result[0][2]
            exec_profile = ExecProfile(
                type_=ExecProfileType(exec_profile["exec_profile_type"]),
                wf_lang=WfLangType(exec_profile["wf_lang_type"]),
            )
            if exec_profile.type_ == ExecProfileType.PYTHON:
                inputs = result[0][4]
                return PythonJob(job_id, job_status, exec_profile, inputs)
            if exec_profile.type_ == ExecProfileType.BASH:
                raise NotImplementedError(
                    "Execution profiles of type Bash not supported, yet"
                )
            raise NotImplementedError(
                "Execution profiles of type WES not supported, yet"
            )

    def update(self, job_id: UUID, job: Job) -> None:
        """Updates a jobs by its id.

        Args:
            job_id (UUID): id of the job
            job (Job): updated job
        """
        with self._engine.connect() as connection:
            connection.execute(
                update(DBJob.__table__)
                .where(DBJob.job_id == str(job_id))
                .values(
                    job_status=job.job_status.value,
                    exec_profile={
                        "exec_profile_type": job.exec_profile.type_.value,
                        "wf_lang_type": job.exec_profile.wf_lang.value,
                    },
                )
            )
