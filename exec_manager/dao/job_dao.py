"""class for job dao"""

from uuid import UUID

from exec_manager.job_status_type import JobStatusType


class JobDAO:
    """
    class for job dao

    ...

    Attributes
    ----------

    Methods
    -------
    update_job_status(self, job_id: UUID, new_job_status: JobStatusType) -> None:
        updates the status of the job in database
    """

    def __init__(self) -> None:
        """constructor"""

    def update_job_status(self, job_id: UUID, new_job_status: JobStatusType) -> None:
        """this method updates the job status"""
