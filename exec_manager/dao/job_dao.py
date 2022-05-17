# Copyright 2021 - 2022 Universität Tübingen, DKFZ and EMBL
# for the German Human Genome-Phenome Archive (GHGA)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""class for job dao"""

import json
from uuid import UUID, uuid4

from sqlalchemy import create_engine, engine, insert, select, update

from exec_manager.dao.db_models import DBJob, metadata
from exec_manager.exec_profile import ExecProfile
from exec_manager.exec_profile_type import ExecProfileType
from exec_manager.job import Job
from exec_manager.job_status_type import JobStatusType
from exec_manager.wf_lang_type import WfLangType

DB_ENGINE = create_engine("sqlite+pysqlite://")
metadata.create_all(DB_ENGINE)


def create_job_dao(
    job_status: JobStatusType,
    exec_profile: ExecProfile,
    workflow: dict,
    inputs: dict,
    db_engine: engine = DB_ENGINE,
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
    engine: engine
        db engine where the connection will be established (default is sqlite with pysqlite)

    Returns
    -------
    UUID
    """
    job_id = generate_job_id()
    job_id_str = str(job_id)
    job_status_str = job_status.value
    exec_profile_json = json.dumps(
        {
            "exec_profile_type": exec_profile.exec_profile_type.value,
            "wf_lang": exec_profile.wf_lang.value,
        }
    )
    inputs_json = json.dumps(inputs)
    with db_engine.connect() as connection:
        connection.execute(
            insert(DBJob.__table__).values(
                (job_id_str, job_status_str, exec_profile_json, workflow, inputs_json)
            )
        )
    return job_id


def get_job(job_id: UUID, db_engine: engine = DB_ENGINE) -> Job:
    """
    Returns a job by his job id.

    Parameters
    ----------
    job_id: UUID
        id of the job
    engine: engine
        db engine where the connection will be established (default is sqlite with pysqlite)

    Returns
    -------
    Job
    """
    with db_engine.connect() as connection:
        cursor = connection.execute(
            select([DBJob.job_id, DBJob.job_status, DBJob.exec_profile]).where(
                DBJob.job_id == str(job_id)
            )
        )
        result = cursor.fetchall()
        job_status = JobStatusType(result[0][1])
        exec_profile = json.loads(result[0][2])
        exec_profile = ExecProfile(
            ExecProfileType(exec_profile["exec_profile_type"]),
            WfLangType(exec_profile["wf_lang"]),
        )
        return Job(job_id, job_status, exec_profile)


def update_job_status(
    job_id: UUID, new_job_status: JobStatusType, db_engine: engine = DB_ENGINE
) -> None:
    """
    Updates a jobs status by his job id.

    Parameters
    ----------
    job_id: UUID
        id of the job
    new_job_status: JobStatusType
        new status of the job; cannot be JobStatusType.NOTSTARTED
    engine: engine
        db engine where the connection will be established (default is sqlite with pysqlite)

    Returns
    -------
    None
    """
    with db_engine.connect() as connection:
        connection.execute(
            update(DBJob.__table__)
            .where(DBJob.job_id == str(job_id))
            .values(job_status=new_job_status.value)
        )


def generate_job_id() -> UUID:
    """
    Generates a unique job id.

    Parameters
    ----------

    Returns
    -------
    UUID
    """
    job_id = uuid4()
    # while get_job(job_id) is not None:
    # job_id = uuid4()
    return job_id
