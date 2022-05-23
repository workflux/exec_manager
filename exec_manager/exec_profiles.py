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

"""module for execution profiles"""

from enum import Enum

from pydantic import BaseModel

from exec_manager.utils import WfLangType


class ExecProfileType(Enum):
    """Enumerate exec profile types:
    - BASH: execution with bash
    - PYTHON: execution with python
    - WES: execution with wes
    """

    BASH = "bash"
    PYTHON = "python"
    WES = "wes"


class ExecProfile(BaseModel):
    """Base model class for execution profiles.

    Args:
        type_ (ExecProfileType): type of the execution profile (Python, Bash or WES)
        wf_lang (WfLangType): language type of workflow (CWL, WDL, Snakemake, Nextflow)
    """

    type_: ExecProfileType
    wf_lang: WfLangType
