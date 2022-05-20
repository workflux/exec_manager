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

from exec_manager.dao.job_dao import create_job_dao, get_job, update_job_status
from exec_manager.exec_profile import ExecProfile
from exec_manager.exec_profile_type import ExecProfileType
from exec_manager.job_status_type import JobStatusType
from exec_manager.wf_lang_type import WfLangType

# import pytest
# from exec_manager.dao.db_models import metadata
# from sqlalchemy import create_engine


# @pytest.fixture
# def example_engine():
#     engine = create_engine("sqlite+pysqlite://")
#     metadata.create_all(engine)
#     return engine


# @pytest.fixture
# def example_job_id():
#     return create_job_dao(
#         JobStatusType.NOTSTARTET,
#         ExecProfile(ExecProfileType.PYTHON, WfLangType.CWL),
#         json.dumps({"test": 1}),
#         {"hello": "world"},
#     )


# engine = create_engine("sqlite+pysqlite://")
# metadata.create_all(engine)
job_status = JobStatusType.NOTSTARTET
exec_profile = ExecProfile(ExecProfileType.PYTHON, WfLangType.CWL)
workflow = {"test": 1}
inputs = {"hello": "world"}
example_job_id = create_job_dao(
    JobStatusType.NOTSTARTET,
    ExecProfile(ExecProfileType.PYTHON, WfLangType.CWL),
    workflow,
    inputs,
)


# @pytest.mark.usefixtures("example_engine")
def test_create_job_dao():
    job_id = create_job_dao(job_status, exec_profile, workflow, inputs)
    db_job = get_job(job_id)
    assert (
        str(db_job.job_id) == str(job_id)
        and db_job.job_status.value == job_status.value
        and (
            json.dumps(
                {
                    "exec_profile_type": db_job.exec_profile.exec_profile_type.value,
                    "wf_lang": db_job.exec_profile.wf_lang.value,
                }
            )
            == json.dumps(
                {
                    "exec_profile_type": ExecProfileType.PYTHON.value,
                    "wf_lang": WfLangType.CWL.value,
                }
            )
        )
    )


# @pytest.mark.usefixtures("example_engine")
def test_get_job():
    job_id = example_job_id
    db_job = get_job(job_id)
    assert (
        str(db_job.job_id) == str(job_id)
        and db_job.job_status.value == job_status.value
        and (
            json.dumps(
                {
                    "exec_profile_type": db_job.exec_profile.exec_profile_type.value,
                    "wf_lang": db_job.exec_profile.wf_lang.value,
                }
            )
            == json.dumps(
                {
                    "exec_profile_type": ExecProfileType.PYTHON.value,
                    "wf_lang": WfLangType.CWL.value,
                }
            )
        )
    )


# @pytest.mark.usefixtures("example_engine")
def test_update_job_status():
    job_id = example_job_id
    update_job_status(job_id, JobStatusType.PREPARING)
    db_job = get_job(job_id)
    assert (
        str(db_job.job_id) == str(job_id)
        and db_job.job_status.value == JobStatusType.PREPARING.value
        and (
            json.dumps(
                {
                    "exec_profile_type": db_job.exec_profile.exec_profile_type.value,
                    "wf_lang": db_job.exec_profile.wf_lang.value,
                }
            )
            == json.dumps(
                {
                    "exec_profile_type": ExecProfileType.PYTHON.value,
                    "wf_lang": WfLangType.CWL.value,
                }
            )
        )
    )
