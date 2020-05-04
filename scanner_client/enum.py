class Enum(object):

    def __init__(self, value):
        self._value = value

    def _eq_(self, instance_or_value):
        if instance_or_value is None:
            return False

        if type(instance_or_value) is Enum:
            return self._value == instance_or_value.value
        return self._value == instance_or_value

    # region "value" accessors

    @property
    def value(self):
        """

        The definition of property "value", which contains the value of the
        enumeration.

        """
        return self._get_value()

    def _get_value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._set_value(val)

    def _set_value(self, val):
        if val is None:
            raise Exception('The provided "value" is not valid')
        self._value = val

    # endregion


__all__ = ['Enum']
