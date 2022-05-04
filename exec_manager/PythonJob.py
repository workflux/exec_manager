from uuid import uuid4
import Job
import ExecProfile
import JobStatusType

class PythonJob(Job):
    def __init__(self, job_id: uuid4, job_status: JobStatusType, exec_profile: ExecProfile) -> None:
        super().__init__(job_id, job_status, exec_profile)
    
    def prepare() -> None:
        pass
    
    def exec() -> None:
        pass
    
    def eval() -> None:
        pass
    
    def finalize() -> None:
        pass
    
    def cancel() -> None:
        pass