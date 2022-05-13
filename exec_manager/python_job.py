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

"""class for python job"""

# from subprocess import Popen  # nosec
from uuid import UUID

from exec_manager.exec_profile import ExecProfile
from exec_manager.job import Job
from exec_manager.job_status_type import JobStatusType


class PythonJob(Job):
    """
    class for python job

    ...

    Attributes
    ----------
    job_id : UUID
        id of the job
    job_status : JobStatusType
        current status of the job (eg. notstarted, succeeded, failed)
    exec_profile : ExecProfile
        python exec profile
    inputs : dict
        input parameters of the job

    Methods
    -------
    prepare() -> None:
        prepares the job
    exec() -> None:
        executes the job
    eval() -> None:
        evaluates the job
    finalize() -> None:
        finalizes the job
    cancel() -> None:
        cancels the job
    """

    def __init__(
        self,
        job_id: UUID,
        job_status: JobStatusType,
        exec_profile: ExecProfile,
        inputs: dict,
    ) -> None:
        """
        Constructs all the necessary attributes for the python job object.

        Parameters
        ----------
        job_id : uuid
            id of the job
        job_status : JobStatusType
            current status of the job (eg. notstarted, succeeded, failed)
        exec_profile : ExecProfile
            python exec profile
        inputs : dict
            input parameters of the job
        py_exec_session : PyExecSession
            session in which the job will be run
        """
        Job.__init__(self, job_id, job_status, exec_profile)
        self.inputs = inputs
        self.wf_lang = exec_profile.wf_lang

    def prepare(self) -> None:
        """
        Prepares the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """

    def exec(self) -> None:
        """
        Executes the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """

    def eval(self) -> None:
        """
        Evaluates the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """

    def finalize(self) -> None:
        """
        Finalizes the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """

    def cancel(self) -> None:
        """
        Cancels the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
