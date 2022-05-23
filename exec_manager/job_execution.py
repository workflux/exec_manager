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
#

"""module for job execution"""

from typing import Callable
from uuid import UUID

from exec_manager.dao.job_dao import SQLJobDAO
from exec_manager.exec_profiles import ExecProfile, ExecProfileType
from exec_manager.jobs import Job, JobStatusType, PythonJob


class PyExecSession:
    """Class for PyExecSession

    Methods:
        run (): runs a job
    """

    def __init__(
        self,
        max_retries: int = 0,
    ) -> None:
        """Constructs all the necessary attributes for the python exec session.

        Args:
            max_retries (int, optional): number of maximum retries when the execution
                fails. Defaults to 0.
        """
        self._max_retries = max_retries

    def run(
        self,
        job_id: UUID,
        job_status: JobStatusType,
        exec_profile: ExecProfile,
        inputs: dict,
    ) -> None:
        """Runs a job.

        Args:
            job_id (UUID): id of the job
            job_status (JobStatusType): current status of the job
                (e.g. notstarted, executing, failed, ...)
            exec_profile (ExecProfile): exec profile with which the job should be
                executed (bash, python, WES)
            inputs (dict): input parameters of the workflow
        """
        counter = -1
        sql_job_dao = SQLJobDAO("sqlite+pysqlite://")
        while self._max_retries > counter:
            python_job = PythonJob(job_id, job_status, exec_profile, inputs)
            python_job.job_status = JobStatusType.PREPARING
            sql_job_dao.update(job_id, python_job)
            python_job.prepare()
            python_job.job_status = JobStatusType.EXECUTING
            sql_job_dao.update(job_id, python_job)
            python_job.exec()
            python_job.job_status = JobStatusType.EVALUATING
            sql_job_dao.update(job_id, python_job)
            python_job.eval()
            python_job.job_status = JobStatusType.FINALZING
            sql_job_dao.update(job_id, python_job)
            python_job.finalize()
            if sql_job_dao.get(job_id).job_status == JobStatusType.SUCCEEDED:
                break
            counter = counter + 1


def create_job(
    inputs: dict,
    workflow: dict,
    exec_profile: ExecProfile,
    create: Callable = SQLJobDAO.create,
) -> Job:
    """Creates a job.

    Args:
        inputs (dict): input paramters of the job
        workflow (dict): the job's workflow
        exec_profile (ExecProfile): exec profile with which the job should be executed
            (bash, python, WES)
        create (Callable, optional): function that stores the job in a database.
            Defaults to SQLJobDAO.create.

    Raises:
        NotImplementedError: Bash execution profile not implemented yet
        NotImplementedError: WES execution profile not implemented yet

    Returns:
        Job: created job
    """
    job_status = JobStatusType.NOTSTARTET
    job_id = create(job_status, exec_profile, workflow, inputs)
    if exec_profile.type_ == ExecProfileType.PYTHON:
        return PythonJob(job_id, job_status, exec_profile, inputs)
    if exec_profile.type_ == ExecProfileType.BASH:
        raise NotImplementedError("Execution profiles of type Bash not supported, yet")
    raise NotImplementedError("Execution profiles of type WES not supported, yet")
