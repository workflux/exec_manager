from enum import Enum


class JobStatusType(Enum):
    NOTSTARTET = "not startetd"
    PREPARING = "preparing"
    EXECUTING = "executing"
    EVALUATING = "evaluating"
    FINALZING = "finalizing"
    CANCELED = "canceled"
    FAILED = "failed"
    SUCCEEDED = "succeeded"
