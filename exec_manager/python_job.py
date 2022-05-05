"""class for python job"""

from uuid import UUID

from exec_manager.dao.job_dao import update_job_status
from exec_manager.exec_profile import ExecProfile
from exec_manager.job import Job
from exec_manager.job_status_type import JobStatusType


class PythonJob(Job):
    """
    class for python job

    ...

    Attributes
    ----------
    job_id : uuid
        id of the job
    job_status : JobStatusType
        current status of the job (eg. notstarted, succeeded, failed)
    exec_profile : ExecProfile
        python exec profile

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
    """

    def __init__(
        self,
        job_id: UUID,
        job_status: JobStatusType,
        exec_profile: ExecProfile,
        inputs: dict,
    ) -> None:
        """Constructs all the necessary attributes for the python job object."""
        Job.__init__(self, job_id, job_status, exec_profile)
        self.inputs = inputs

    def prepare(self) -> None:
        """
        Prepares the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        # JobDAO.update_job_status(self.job_id, JobStatusType.PREPARING)

    def exec(self) -> None:
        """
        Executes the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        update_job_status(self.job_id, JobStatusType.EXECUTING)
        command_list = [self.exec_profile, self.inputs]
        print(command_list)

    def eval(self) -> None:
        """
        Evaluates the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        # job_dao = JobDAO()
        # job_dao.update_job_status(self.job_id, JobStatusType.EVALUATING)

    def finalize(self) -> None:
        """
        Finalizes the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        # job_dao = JobDAO()
        # job_dao.update_job_status(self.job_id, JobStatusType.FINALZING)

    def cancel(self) -> None:
        """
        Cancels the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        # job_dao = JobDAO()
        # job_dao.update_job_status(self.job_id, JobStatusType.CANCELED)
