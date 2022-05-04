"""class for job factory"""

from exec_manager.exec_profile import ExecProfile
from exec_manager.job import Job


class JobFactory:
    """
    class for job factory

    ...

    Attributes
    ----------

    Methods
    -------
    create_job(inputs: dict, workflow, exec_profile: ExecProfile) -> Job:
        creates a new job
    """

    def __init__(self) -> None:
        """this is the constructor"""

    def create_job(self, inputs: dict, workflow, exec_profile: ExecProfile) -> Job:
        """this method creates a new job"""
