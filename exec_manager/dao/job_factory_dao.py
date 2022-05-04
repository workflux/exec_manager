"""class for job factory dao"""

from uuid import UUID

from exec_manager.exec_profile import ExecProfile
from exec_manager.job_status_type import JobStatusType


class JobFactoryDAO:
    """
    class for job factory dao

    ...

    Attributes
    ----------

    Methods
    -------
    create_job(
        self,
        job_status: JobStatusType,
        inputs: dict,
        workflow,
        exec_profile: ExecProfile,
    ) -> uuid:
        inserts job into database
    """

    def __init__(self) -> None:
        """constructor"""

    def create_job(
        self,
        job_status: JobStatusType,
        inputs: dict,
        workflow,
        exec_profile: ExecProfile,
    ) -> UUID:
        """this method creates a job"""
