import uuid

import exec_manager.job_status_type as job_status_type


class JobDAO:
    def __init__(self) -> None:
        pass

    def update_job_status(self, job_id: uuid, new_job_status: job_status_type) -> None:
        pass
