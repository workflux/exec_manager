import uuid

import exec_manager.exec_profile as exec_profile
import exec_manager.job as job
import exec_manager.job_status_type as job_status_type


class PythonJob(job):
    def __init__(
        self, job_id: uuid, job_status: job_status_type, exec_profile: exec_profile
    ) -> None:
        super().__init__(job_id, job_status, exec_profile)

    def prepare(self) -> None:
        pass

    def exec(self) -> None:
        pass

    def eval(self) -> None:
        pass

    def finalize(self) -> None:
        pass

    def cancel(self) -> None:
        pass
