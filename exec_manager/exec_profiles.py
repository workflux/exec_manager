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
    """
    class for Exec-Profile

    ...

    Attributes
    ----------
    exec_profile_type : ExecProfileType
        type of the exec profile (bash, python, wes)
    wf_lang : WfLangType
        workflow language (cwl, wdl, nextflow, snakemake)

    Methods
    -------
    """

    type_: ExecProfileType
    wf_lang: WfLangType
