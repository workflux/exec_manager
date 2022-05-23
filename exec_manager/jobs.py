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

"""module for jobs"""

from abc import ABC, abstractmethod
from enum import Enum
from uuid import UUID

from exec_manager.exec_profiles import ExecProfile


class JobStatusType(Enum):
    """Enumerate job status types:
    - NOTSTARTET: job is not started yet
    - PREPARING: job is preparing
    - EXECUTING: job is executing
    - EVALUATING: job is evaluating
    - FINALZING: job is finalizing
    - CANCELED: job is canceled
    - FAILED: job is failed
    - SUCCEEDED: job is succeeded
    """

    NOTSTARTET = "not started"
    PREPARING = "preparing"
    EXECUTING = "executing"
    EVALUATING = "evaluating"
    FINALZING = "finalizing"
    CANCELED = "canceled"
    FAILED = "failed"
    SUCCEEDED = "succeeded"


class Job(ABC):
    """
    class for job

    ...

    Attributes
    ----------
    job_id : uuid
        id of the job
    job_status : JobStatusType
        current status of the job (eg. notstarted, succeeded, failed)
    exec_profile : ExecProfile
        exec profile with which the job should be executed

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
        self, job_id: UUID, job_status: JobStatusType, exec_profile: ExecProfile
    ) -> None:
        """
        Constructs all the necessary attributes for the job object.

        Parameters
        ----------
        job_id : UUID
            id of the job
        job_status : JobStatusType
            current status of the job (eg. notstarted, succeeded, failed, ...)
        exec_profile : ExecProfile
            exec profile with which the job should be executed (bash, python, WES)
        """
        self.job_id = job_id
        self.job_status = job_status
        self.exec_profile = exec_profile

    @abstractmethod
    def prepare(self) -> None:
        """
        Prepares the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        ...

    @abstractmethod
    def exec(self) -> None:
        """
        Executes the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        ...

    @abstractmethod
    def eval(self) -> None:
        """
        Evaluates the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        ...

    @abstractmethod
    def finalize(self) -> None:
        """
        Finalizes the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        ...

    @abstractmethod
    def cancel(self) -> None:
        """
        Cancels the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        ...


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
