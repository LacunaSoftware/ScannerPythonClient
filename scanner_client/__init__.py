"""
Import all elements of the library to facilitate its importation from user.
"""
import scanner_client.rest_client

from scanner_client.rest_client import RestClient

__all__ = []
__all__ += scanner_client.rest_client.__all__