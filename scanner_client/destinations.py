from .enum import Enum


class Destinations (Enum):
    TRANSFER = 'Transfer'
    DESTRUCTION = 'Destruction'
    STORAGE = 'Storage'

__all__ = ['Destinations']