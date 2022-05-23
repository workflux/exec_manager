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
    """abstract class for job

    Args:
        job_id (UUID): id of the job
        job_status (JobStatusType): current status of the job (eg. notstarted, succeeded, failed)
        exec_profile (ExecProfile): exec profile with which the job should be executed

    Methods:
        prepare (): prepares the job
        exec (): executes the job
        eval (): evaluates the job
        finalize (): finalizes the job
        cancel (): cancels the job

    """

    def __init__(
        self, job_id: UUID, job_status: JobStatusType, exec_profile: ExecProfile
    ) -> None:
        """Constructs all the necessary attributes for the job object.

        Args:
            job_id (UUID): id of the job
            job_status (JobStatusType): current status of the job
                (eg. notstarted, succeeded, failed, ...)
            exec_profile (ExecProfile): exec profile with which the job should be
                executed (bash, python, WES)
        """
        self.job_id = job_id
        self.job_status = job_status
        self.exec_profile = exec_profile

    @abstractmethod
    def prepare(self) -> None:
        """Prepares the job."""
        ...

    @abstractmethod
    def exec(self) -> None:
        """Executes the job."""
        ...

    @abstractmethod
    def eval(self) -> None:
        """Evaluates the job."""
        ...

    @abstractmethod
    def finalize(self) -> None:
        """Finalizes the job."""
        ...

    @abstractmethod
    def cancel(self) -> None:
        """Cancels the job."""
        ...


class PythonJob(Job):
    """
    class for python job

    Args:
        job_id (UUID): id of the job
        job_status (JobStatusType): current status of the job (eg. notstarted, succeeded, failed)
        exec_profile (ExecProfile): python exec profile
        inputs (dict): input parameters of the job

    Methods:
        prepare (): prepares the job
        exec (): executes the job
        eval (): evaluates the job
        finalize (): finalizes the job
        cancel (): cancels the job
    """

    def __init__(
        self,
        job_id: UUID,
        job_status: JobStatusType,
        exec_profile: ExecProfile,
        inputs: dict,
    ) -> None:
        """Constructs all the necessary attributes for the python job object.

        Args:
            job_id (UUID): id of the job
            job_status (JobStatusType): current status of the job
                (eg. notstarted, succeeded, failed)
            exec_profile (ExecProfile): python exec profile
            inputs (dict): input parameters of the job
        """
        Job.__init__(self, job_id, job_status, exec_profile)
        self.inputs = inputs
        self.wf_lang = exec_profile.wf_lang

    def prepare(self) -> None:
        """Prepares the job."""
        ...

    def exec(self) -> None:
        """Executes the job."""
        ...

    def eval(self) -> None:
        """Evaluates the job."""
        ...

    def finalize(self) -> None:
        """Finalizes the job."""
        ...

    def cancel(self) -> None:
        """Cancels the job."""
        ...
