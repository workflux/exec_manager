"""class for job factory"""

import job

from exec_manager.exec_profile import ExecProfile


class JobFactory:
    """
    class for job factory

    ...

    Attributes
    ----------

    Methods
    -------
    create_job(inputs: dict, workflow, exec_profile: ExecProfile) -> job:
        creates a new job
    """

    def __init__(self) -> None:
        """this is the constructor"""

    def create_job(self, inputs: dict, workflow, exec_profile: ExecProfile) -> job:
        """this method creates a new job"""
