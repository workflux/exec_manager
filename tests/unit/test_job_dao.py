# Copyright 2021 - 2022 German Cancer Research Center (DKFZ)
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

import json
from typing import Generator
from uuid import UUID

import pytest

from exec_manager.dao.job_dao import SQLJobDAO
from exec_manager.exec_profiles import ExecProfile, ExecProfileType
from exec_manager.jobs import JobStatusType, PythonJob
from exec_manager.utils import WfLangType


@pytest.fixture
def example_sqlite_job_dao() -> Generator:
    """
    Creates sqlite engine.

    Parameters
    ----------

    Returns
    -------
    None
    """
    engine = SQLJobDAO("sqlite+pysqlite://")
    yield engine


@pytest.fixture
def example_job_status() -> JobStatusType:
    """
    Creates a job status.

    Parameters
    ----------

    Returns
    -------
    JobStatusType
    """
    return JobStatusType.NOTSTARTET


@pytest.fixture
def example_exec_profile() -> ExecProfile:
    """
    Creates an exec profile.

    Parameters
    ----------

    Returns
    -------
    ExecProfile
    """
    return ExecProfile(type_=ExecProfileType.PYTHON, wf_lang=WfLangType.CWL)


@pytest.fixture
def example_workflow() -> dict:
    """
    Creates a workflow.

    Parameters
    ----------

    Returns
    -------
    dict
    """
    return {"test": 1}


@pytest.fixture
def example_inputs() -> dict:
    """
    Creates inputs.

    Parameters
    ----------

    Returns
    -------
    dict
    """
    return {"hello": "world"}


@pytest.fixture
def example_job_id(
    example_job_status: JobStatusType,
    example_exec_profile: ExecProfile,
    example_workflow: dict,
    example_inputs: dict,
    example_sqlite_job_dao,
) -> UUID:
    """
    Creates a job id.

    Parameters
    ----------
    example_job_status: JobStatusType
        status of the job
    example_exec_profile: ExecProfile
        execution profile of the job
    example_workflow: dict
        job's workflow
    example_inputs: dict
        input parameters of the workflow
    example_sqlite_job_dao
        database engine

    Returns
    -------
    UUID
    """
    return example_sqlite_job_dao.create(
        example_job_status,
        example_exec_profile,
        example_workflow,
        example_inputs,
    )


@pytest.mark.usefixtures(
    "example_sqlite_job_dao",
    "example_job_id",
    "example_exec_profile",
    "example_workflow",
    "example_inputs",
)
def test_create(
    example_job_status: JobStatusType,
    example_exec_profile: ExecProfile,
    example_workflow: dict,
    example_inputs: dict,
    example_sqlite_job_dao,
) -> None:
    """
    Tests the create method from SQLJobDAO class.

    Parameters
    ----------
    example_job_status: JobStatusType
        status of the job
    example_exec_profile: ExecProfile
        execution profile of the job
    example_workflow: dict
        job's workflow
    example_inputs: dict
        input parameters of the workflow
    example_sqlite_job_dao
        database engine

    Returns
    -------
    None
    """
    job_id = example_sqlite_job_dao.create(
        example_job_status,
        example_exec_profile,
        example_workflow,
        example_inputs,
    )
    db_job = example_sqlite_job_dao.get(job_id)
    assert (
        str(db_job.job_id) == str(job_id)
        and db_job.job_status.value == example_job_status.value
        and (
            json.dumps(
                {
                    "exec_profile_type": db_job.exec_profile.type_.value,
                    "wf_lang": db_job.exec_profile.wf_lang.value,
                }
            )
            == json.dumps(
                {
                    "exec_profile_type": example_exec_profile.type_.value,
                    "wf_lang": example_exec_profile.wf_lang.value,
                }
            )
        )
    )


@pytest.mark.usefixtures(
    "example_sqlite_job_dao", "example_job_id", "example_exec_profile"
)
def test_get(
    example_job_id: UUID,
    example_job_status: JobStatusType,
    example_exec_profile: ExecProfile,
    example_sqlite_job_dao,
) -> None:
    """
    Tests the get method from SQLJobDAO class.

    Parameters
    ----------
    example_job_id: UUID
        id of the job
    example_job_status: JobStatusType
        status of the job
    example_exec_profile: ExecProfile
        execution profile of the job
    example_sqlite_job_dao
        database engine

    Returns
    -------
    None
    """
    job_id = example_job_id
    db_job = example_sqlite_job_dao.get(job_id)
    assert (
        str(db_job.job_id) == str(job_id)
        and db_job.job_status.value == example_job_status.value
        and (
            json.dumps(
                {
                    "exec_profile_type": db_job.exec_profile.type_.value,
                    "wf_lang": db_job.exec_profile.wf_lang.value,
                }
            )
            == json.dumps(
                {
                    "exec_profile_type": example_exec_profile.type_.value,
                    "wf_lang": example_exec_profile.wf_lang.value,
                }
            )
        )
    )


@pytest.mark.usefixtures(
    "example_sqlite_job_dao", "example_job_id", "example_exec_profile"
)
def test_update(
    example_job_id: UUID,
    example_exec_profile: ExecProfile,
    example_inputs: dict,
    example_sqlite_job_dao,
) -> None:
    """
    Tests the update method from SQLJobDAO class.

    Parameters
    ----------
    example_job_id: UUID
        id of the job
    example_exec_profile: ExecProfile
        execution profile of the job
    example_inputs: dict
        input parameters of the workflow
    example_sqlite_job_dao: Engine
        database engine

    Returns
    -------
    None
    """
    job_id = example_job_id
    job = PythonJob(
        job_id, JobStatusType.PREPARING, example_exec_profile, example_inputs
    )
    example_sqlite_job_dao.update(job_id, job)
    db_job = example_sqlite_job_dao.get(job_id)
    assert (
        str(db_job.job_id) == str(job_id)
        and db_job.job_status.value == JobStatusType.PREPARING.value
        and (
            {
                "exec_profile_type": db_job.exec_profile.type_.value,
                "wf_lang": db_job.exec_profile.wf_lang.value,
            }
            == {
                "exec_profile_type": example_exec_profile.type_.value,
                "wf_lang": example_exec_profile.wf_lang.value,
            }
        )
    )
