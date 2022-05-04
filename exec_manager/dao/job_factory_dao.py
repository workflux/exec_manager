import uuid

import exec_manager.exec_profile as exec_profile
import exec_manager.job_status_type as job_status_type


class JobFactoryDAO:
    def __init__(self) -> None:
        pass

    def create_job(
        self,
        job_status: job_status_type,
        inputs: dict,
        workflow,
        exec_profile: exec_profile,
    ) -> uuid:
        pass
