from .administrative_metadata import AdministrativeMetadata
from .descriptive_metadata import DescriptiveMetadata
from .digest_algorithm_and_value import DigestAlgorithmAndValue

class Document:
    def __init__(self, client, model):
        self._client = client
        self._id = model['id']
        self._file_name = model['fileName']
        self._content_length = model['contentLength']
        self._content_type = model['contentType']

        if model['hash']:
            self._hash = DigestAlgorithmAndValue(model['hash'])
        
        if model['descriptiveMetadata']: 
            self._descriptive_metadata = DescriptiveMetadata(model['descriptiveMetadata'])
        
        if model['administrativeMetadata']:
            self._administrative_metadata = AdministrativeMetadata(model['administrativeMetadata'])

    def get_download_link(self):
        return self._client.get_document_download_link(self._id)

    def open_read(self):
        return self._client.open_read_document(self._id)

    def get_content(self):
        return self._client.get_document_content(self._id)

    def get_metadata_file_download_link(self):
        return self._client.get_document_metadata_file_download_link(self._id)

    def open_read_metadata_file(self):
        return self._client.open_read_document_metadata_file(self._id)

    def get_metadata_file_content(self):
        return self._client.get_document_metadata_file_content(self._id)

__all__ = ['Document']