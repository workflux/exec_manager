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

"""class for exec profile"""

from pydantic import BaseModel

from exec_manager.exec_profile_type import ExecProfileType
from exec_manager.wf_lang_type import WfLangType


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
