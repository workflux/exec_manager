"""class for job dao"""

from uuid import UUID, uuid4

from sqlalchemy import engine_from_config
from sqlalchemy.orm import Session

from exec_manager.dao.db_models import DBJob
from exec_manager.exec_profile import ExecProfile
from exec_manager.job import Job
from exec_manager.job_status_type import JobStatusType


class JobDAO:
    """
    class for job dao

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
    ) -> UUID:
        creates a job

    update_job_status(self, job_id: UUID, new_job_status: JobStatusType) -> None:
        updates the status of the job in database

    get_job(job_id: UUID) -> Job:
        returns a job by the job id

    generate_job_id() -> UUID:
        generates a uuid as job id and checks its uniqueness
    """

    def __init__(self) -> None:
        """constructor"""


def create_job_dao(
    job_status: JobStatusType,
    exec_profile: ExecProfile,
    workflow,
    inputs: dict,
) -> UUID:
    """
    Inserts a job into the database.

    Parameters
    ----------
    job_status: JobStatusType
        current status of the job; initially it is JobStatusType.NOTSTARTED
    exec_profile: ExecProfile
        exec profile of this job
    workflow
        the jobs workflow
    inputs: dict
        the input parameters of the job

    Returns
    -------
    UUID
    """

    job_id = generate_job_id()
    with Session(engine_from_config) as session:
        with session.begin():
            session.insert(DBJob).values(
                job_id, job_status, exec_profile, workflow, inputs
            )
    return job_id


def generate_job_id() -> UUID:
    """
    Generates an unique job id.

    Parameters
    ----------

    Returns
    -------
    UUID
    """
    job_id = uuid4()
    while get_job(job_id) is not None:
        job_id = uuid4()
    return job_id


def update_job_status(job_id: UUID, new_job_status: JobStatusType) -> None:
    """
    Updates a jobs status by his job id.

    Parameters
    ----------
    job_id: UUID
        id of the job
    new_job_status: JobStatusType
        new status of the job; cannot be JobStatusType.NOTSTARTED

    Returns
    -------
    None
    """
    with Session(engine_from_config) as session:
        with session.begin():
            session.update(DBJob).where(DBJob.job_id == job_id).values(
                job_status=new_job_status
            )


def get_job(job_id: UUID) -> Job:
    """
    Returns a job by his job id.

    Parameters
    ----------
    job_id: UUID
        id of the job

    Returns
    -------
    Job
    """
    with Session(engine_from_config) as session:
        with session.begin():
            return session.query(DBJob).filter_by(job_id=job_id).all()
