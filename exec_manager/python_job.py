"""class for python job"""

from uuid import UUID

from exec_manager.exec_profile import ExecProfile
from exec_manager.job_status_type import JobStatusType


class PythonJob:
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
        self, job_id: UUID, job_status: JobStatusType, exec_profile: ExecProfile
    ) -> None:
        """constructor"""

    def prepare(self) -> None:
        """job preparation"""

    def exec(self) -> None:
        """job execution"""

    def eval(self) -> None:
        "job evaluation"

    def finalize(self) -> None:
        """job finalization"""

    def cancel(self) -> None:
        """job canceling"""
