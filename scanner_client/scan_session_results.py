from .enum import Enum


class ScanSessionResults (Enum):
    SUCCESS = 'Success'
    USER_CANCELLED = 'UserCancelled'

__all__ = ['ScanSessionResults']