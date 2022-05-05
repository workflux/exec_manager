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

"""Defines all database specific ORM models"""

from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta

from exec_manager.exec_profile import ExecProfile

Base: DeclarativeMeta = declarative_base()


class DBJob(Base):
    """An job object stored in the DB"""

    __tablename__ = "job"
    job_id = Column(String, primary_key=True)
    job_status = Column(String, nullable=False)
    exec_profile = Column(JSON, nullable=False)
    workflow = Column(JSON, nullable=False)
    inputs = Column(JSON, nullable=False)
