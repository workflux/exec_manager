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
