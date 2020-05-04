class MetadataPresets():
    def __init__(self):
        self._document_type = None
        self._document_type_is_readonly = None

    def _get_document_type_is_readonly(self):
        return self._document_type_is_readonly

    def _set_document_type_is_readonly(self, value):
        if not value:
            raise Exception('The provided "endpoint_url" is not valid')
        self._document_type_is_readonly = value

    document_type_is_readonly = property(_get_document_type_is_readonly, _set_document_type_is_readonly)

    def _get_document_type(self):
        return self._document_type

    def _set_document_type(self, value):
        if not value:
            raise Exception('The provided "endpoint_url" is not valid')
        self._document_type = value

    document_type = property(_get_document_type, _set_document_type)

__all__ = ['MetadataPresets']