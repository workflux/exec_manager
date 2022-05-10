# Copyright 2021 - 2022 Universität Tübingen, DKFZ and EMBL
# for the German Human Genome-Phenome Archive (GHGA)
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

"""enum for job status type"""

from enum import Enum


class JobStatusType(Enum):
    """enumerate job status types"""

    NOTSTARTET = "not startetd"
    """job ist not started yet"""

    PREPARING = "preparing"
    """job is preparing"""

    EXECUTING = "executing"
    """job is executing"""

    EVALUATING = "evaluating"
    """job ist evaluating"""

    FINALZING = "finalizing"
    """job is finalizing"""

    CANCELED = "canceled"
    """job is canceled"""

    FAILED = "failed"
    """job is failed"""

    SUCCEEDED = "succeeded"
    """job is succeeded"""
