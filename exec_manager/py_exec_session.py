# Copyright 2021 - 2022 Universität Tübingen, DKFZ and EMBL
# for the German Human Genome-Phenome Archive (GHGA)
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

"""class for python exec session"""


from uuid import UUID

from exec_manager.dao.job_dao import get_job, update_job_status
from exec_manager.exec_profile import ExecProfile
from exec_manager.job_status_type import JobStatusType
from exec_manager.python_job import PythonJob


class PyExecSession:
    """
    class for python job

    ...

    Attributes
    ----------
    max_retries : int

    Methods
    -------
    start() -> None
        starts a session
    """

    def __init__(
        self,
        max_retries: int = 0,
    ) -> None:
        """
        Constructs all the necessary attributes for the python exec session.

        Parameters
        ----------
        max_retries : int
        """
        self.max_retries = max_retries

    def run(
        self,
        job_id: UUID,
        job_status: JobStatusType,
        exec_profile: ExecProfile,
        inputs: dict,
    ) -> None:
        """
        Starts the session.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        counter = -1
        while self.max_retries > counter:
            python_job = PythonJob(job_id, job_status, exec_profile, inputs)
            update_job_status(job_id, JobStatusType.PREPARING)
            python_job.prepare()
            update_job_status(job_id, JobStatusType.EXECUTING)
            python_job.exec()
            update_job_status(job_id, JobStatusType.EVALUATING)
            python_job.eval()
            update_job_status(job_id, JobStatusType.FINALZING)
            python_job.finalize()
            if get_job(job_id).job_status == JobStatusType.SUCCEEDED:
                break
            counter = counter + 1
