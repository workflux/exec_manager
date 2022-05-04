"""enum for exec profile type"""

from enum import Enum


class ExecProfileType(Enum):
    """enumaerate exec profile types"""

    BASH = "bash"
    """execution with bash"""

    PYTHON = "python"
    """execution with python"""

    WES = "wes"
    """execution with wes"""
