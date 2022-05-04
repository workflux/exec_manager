from uuid import uuid4
import JobStatusType
import WfLangType
import ExecProfile


class JobFactoryDAO:
    def __init__(self) -> None:
        pass

    def create_job(job_status: JobStatusType, inputs: dict, workflow, wf_lang: WfLangType, exec_profile: ExecProfile) -> uuid4:
        pass