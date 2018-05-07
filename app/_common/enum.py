from enum import Enum


class BuildStatus(Enum):
    QUEUED = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    FAILED = 4
