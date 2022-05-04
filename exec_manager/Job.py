from abc import abstractmethod
from sys import exec_prefix
from uuid import uuid4

import JobStatusType
import ExecProfile


class Job:
    def __init__(self, job_id: uuid4, job_status: JobStatusType, exec_profile: ExecProfile) -> None:
        self.job_id = job_id
        self.job_status=job_status
        self.exec_profile=exec_profile
    
    @abstractmethod
    def prepare() -> None:
        """This method should implement the prepare execution step"""
    
    @abstractmethod
    def exec() -> None:
        """This method should implement the exec execution step"""
    
    @abstractmethod
    def eval() -> None:
        """This method should implement the eval execution step"""
    
    @abstractmethod
    def finalize() -> None:
        """This method should implement the finalize execution step"""
    
    @abstractmethod
    def cancel() -> None:
        """This method should implement the cancel execution step"""
    