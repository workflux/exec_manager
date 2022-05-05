"""class for job factory"""

from exec_manager.dao.job_dao import create_job_dao
from exec_manager.exec_profile import ExecProfile
from exec_manager.exec_profile_type import ExecProfileType
from exec_manager.job import Job
from exec_manager.job_status_type import JobStatusType
from exec_manager.python_job import PythonJob


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


def create_job(inputs: dict, workflow, exec_profile: ExecProfile) -> Job:
    """
    Creates a job.

    Parameters
    ----------

    Returns
    -------
    Job
    """
    job_status = JobStatusType.NOTSTARTET
    job_id = create_job_dao(job_status, exec_profile, workflow, inputs)
    if exec_profile.exec_profile_type == ExecProfileType.PYTHON:
        return PythonJob(job_id, job_status, exec_profile, inputs)
    if exec_profile.exec_profile_type == ExecProfileType.BASH:
        pass  # place for bash job
    if exec_profile.exec_profile_type == ExecProfileType.WES:
        pass  # place for wes job
    return Job(job_id, job_status, exec_profile)
