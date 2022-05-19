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

"""class for job factory"""

from typing import Callable

from exec_manager.dao.job_dao import create_job_dao
from exec_manager.exec_profile import ExecProfile
from exec_manager.exec_profile_type import ExecProfileType
from exec_manager.job import Job
from exec_manager.job_status_type import JobStatusType
from exec_manager.python_job import PythonJob


def create_job(
    inputs: dict,
    workflow,
    exec_profile: ExecProfile,
    create_dao_job: Callable = create_job_dao,
) -> Job:
    """
    Creates a job.

    Parameters
    ----------

    Returns
    -------
    Job
    """
    job_status = JobStatusType.NOTSTARTET
    job_id = create_dao_job(job_status, exec_profile, workflow, inputs)
    if exec_profile.exec_profile_type == ExecProfileType.PYTHON:
        return PythonJob(job_id, job_status, exec_profile, inputs)
    elif exec_profile.exec_profile_type == ExecProfileType.BASH:
        raise NotImplementedError("Execution profiles of type Bash not supported, yet")
    else:
        raise NotImplementedError("Execution profiles of type WES not supported, yet")
