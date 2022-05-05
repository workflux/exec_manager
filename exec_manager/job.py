"""class for job"""

from uuid import UUID

from exec_manager.exec_profile import ExecProfile
from exec_manager.job_status_type import JobStatusType


class Job:
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
        job_id : uuid
            id of the job
        job_status : JobStatusType
            current status of the job (eg. notstarted, succeeded, failed)
        exec_profile : ExecProfile
            exec profile with which the job should be executed
        """
        self.job_id = job_id
        self.job_status = job_status
        self.exec_profile = exec_profile

    def prepare(self) -> None:
        """This method should implement the prepare execution step"""

    def exec(self) -> None:
        """This method should implement the exec execution step"""

    def eval(self) -> None:
        """This method should implement the eval execution step"""

    def finalize(self) -> None:
        """This method should implement the finalize execution step"""

    def cancel(self) -> None:
        """This method should implement the cancel execution step"""
