import json

from exec_manager.dao.job_dao import create_job_dao, get_job, update_job_status
from exec_manager.exec_profile import ExecProfile
from exec_manager.exec_profile_type import ExecProfileType
from exec_manager.job_status_type import JobStatusType
from exec_manager.wf_lang_type import WfLangType

# from uuid import UUID


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
workflow = "test_workflow.json"  # {"test" : 1}
inputs = {"hello": "world"}
example_job_id = create_job_dao(
    JobStatusType.NOTSTARTET,
    ExecProfile(ExecProfileType.PYTHON, WfLangType.CWL),
    json.dumps({"test": 1}),
    {"hello": "world"},
)


def test_create_job_dao():
    job_status = JobStatusType.NOTSTARTET
    exec_profile = ExecProfile(ExecProfileType.PYTHON, WfLangType.CWL)
    workflow = json.dumps({"test": 1})
    inputs = {"hello": "world"}
    job_id = create_job_dao(
        job_status,
        exec_profile,
        workflow,
        inputs,
    )
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


# convert every object to string to check if the content of the objects are equal
def test_get_job():
    job_id = example_job_id
    db_job = get_job(job_id)
    assert (
        str(db_job.job_id) == str(job_id)
        and db_job.job_status.value == JobStatusType.NOTSTARTET.value
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


def test_update_job_status():
    job_id = example_job_id
    update_job_status(job_id, JobStatusType.NOTSTARTET)
    db_job = get_job(job_id)
    assert (
        str(db_job.job_id) == str(job_id)
        and db_job.job_status.value == JobStatusType.NOTSTARTET.value
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
