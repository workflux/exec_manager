import uuid
from abc import abstractmethod

import exec_manager.exec_profile as exec_profile
import exec_manager.job_status_type as job_status_type


class Job:
    def __init__(
        self, job_id: uuid, job_status: job_status_type, exec_profile: exec_profile
    ) -> None:
        self.job_id = job_id
        self.job_status = job_status
        self.exec_profile = exec_profile

    @abstractmethod
    def prepare(self) -> None:
        """This method should implement the prepare execution step"""

    @abstractmethod
    def exec(self) -> None:
        """This method should implement the exec execution step"""

    @abstractmethod
    def eval(self) -> None:
        """This method should implement the eval execution step"""

    @abstractmethod
    def finalize(self) -> None:
        """This method should implement the finalize execution step"""

    @abstractmethod
    def cancel(self) -> None:
        """This method should implement the cancel execution step"""
