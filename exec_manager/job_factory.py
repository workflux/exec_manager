import exec_manager.exec_profile as exec_profile
import exec_manager.job as job


class JobFactory:
    def __init__(self) -> None:
        pass

    def create_job(self, inputs: dict, workflow, exec_profile: exec_profile) -> job:
        pass
