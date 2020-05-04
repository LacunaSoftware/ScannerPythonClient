import binascii

from .digest_algorithm import DigestAlgorithm
from .utils import _base64_decode


class DigestAlgorithmAndValue(object):

    def __init__(self, model):

        self._algorithm = None
        algorithm = model.get('algorithm', None)
        if algorithm is not None:
            self._algorithm = \
                DigestAlgorithm.get_instance_by_api_model(str(algorithm))

        self._value = None
        value = model.get('value', None)
        if value is not None:
            self._value = _base64_decode(value)

    @property
    def algorithm(self):
        return self._algorithm

    @algorithm.setter
    def algorithm(self, value):
        self._algorithm = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

    @property
    def hex_value(self):
        return binascii.hexlify(self._value)

    @hex_value.setter
    def hex_value(self, value):
        self._value = binascii.unhexlify(value)

    def to_model(self):
        return {
            'algorithm': self._algorithm.api_model,
            'value': self._value
        }


__all__ = ['DigestAlgorithmAndValue']
