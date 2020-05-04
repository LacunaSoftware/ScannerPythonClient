from .document import Document
from .rest_client import RestClient
from .create_scan_session_response import CreateScanSessionResponse
from .scan_session import ScanSession


class ScannerClient:
    def __init__(self, options):
        self._options = options
        self._rest_client = None

    # region Scan Sessions

    def create_scan_session(self, return_url, multifile = False, metadata_presets = None, subscription_id = None):
        request = {
            'returnUrl': return_url,
            'multifile': multifile,
            'metadataPresets': metadata_presets,
        }
        custom_headers = {}
        if subscription_id:
            custom_headers['X-Subscription'] = subscription_id
        client = self._get_rest_client(custom_headers)

        response = client.post('/api/scan-sessions', request)
        return CreateScanSessionResponse(response)

    def get_scan_session(self, scan_session_id):
        client = self._get_rest_client()
        response = client.get("/api/scan-sessions/%s" % scan_session_id)
        return ScanSession(self, response)

    # endregion

    # region Documents

    def get_document(self, document_id):
        client = self._get_rest_client()
        response = client.get("/api/documents/%s" % document_id)
        return Document(self, response)

    def get_document_download_link(self, document_id):
        client = self._get_rest_client()
        return client.get("/api/documents/%s/file-link" % document_id)

    def open_read_document(self, document_id):
        client = self._get_rest_client()
        download_link = self.get_document_download_link(document_id)
        return client.open_read(download_link)

    def get_document_content(self, document_id):
        stream = self.open_read_document(document_id)
        return stream.content

    def get_document_metadata_file_download_link(self, document_id):
        client = self._get_rest_client()
        return client.get("/api/documents/%s/metadata-file-link" % document_id)

    def open_read_document_metadata_file(self, document_id):
        client = self._get_rest_client()
        download_link = self.get_document_metadata_file_download_link(document_id)
        return client.open_read(download_link)

    def get_document_metadata_file_content(self, document_id):
        stream = self.open_read_document_metadata_file(document_id)
        return stream.content

    # endregion

    def _get_rest_client(self, custom_request_headers=None):
        if not self._rest_client:
            self._rest_client = RestClient(
                self._options.endpoint,
                self._options.api_key
            )
        if custom_request_headers:
            self._rest_client.custom_request_headers = custom_request_headers
        return self._rest_client

__all__ = ['ScannerClient']