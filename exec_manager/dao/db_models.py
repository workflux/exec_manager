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

"""Defines all database specific ORM models"""

import uuid

from sqlalchemy import JSON, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta

Base: DeclarativeMeta = declarative_base()
metadata = Base.metadata

# this method is neccessary to avoid IntegrityError
def generate_uuid_str() -> str:
    """Generates a uuid with type string.

    Returns:
        str: job id
    """
    return str(uuid.uuid4())


class DBJob(Base):
    """An job object stored in the DB"""

    __tablename__ = "job"

    job_id = Column(String, default=generate_uuid_str, primary_key=True)
    job_status = Column(String, nullable=False)
    exec_profile = Column(JSON, nullable=False)
    workflow = Column(JSON, nullable=False)
    inputs = Column(JSON, nullable=False)
