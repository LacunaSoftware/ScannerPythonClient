import hashlib
import requests
import simplejson as json

from .rest_error import RestError
from .rest_unreachable_error import RestUnreachableError
from .scanner_error import ScannerError
from .validation import ValidationResults
from .validation_error import ValidationError

class RestClient(object):

    def __init__(self, endpoint_url, api_key, custom_request_headers=None):
        self._endpoint_url = endpoint_url
        self._api_key = api_key
        self._multipart_upload_double_check = None
        self._multipart_upload_threshold = 5 * 1024 * 1024  # 5MB
        self._custom_request_headers = custom_request_headers

    def get_request_headers(self):
        headers = {
            'Accept': 'application/json',
            'X-Api-Key': '%s' % self._api_key,
            'Content-Type': 'application/json',
            'charset': 'utf8'
        }
        if self._custom_request_headers:
            headers.update(self._custom_request_headers)
        return headers

    def get(self, url, params=None):
        verb = 'GET'
        try:
            response = requests.get('%s%s' % (self._endpoint_url, url),
                                    params=params,
                                    headers=self.get_request_headers())
        except Exception:
            raise RestUnreachableError(verb, url)

        self._check_response(verb, url, response)
        return response.json()

    def open_read(self, url):
        verb = 'GET'
        try:
            response = requests.get('%s%s' % (self._endpoint_url, url),
                                    stream=True,
                                    headers=self.get_request_headers())
        except Exception:
            raise RestUnreachableError(verb, url)

        self._check_response(verb, url, response)
        return response

    def post(self, url, data=None):
        verb = 'POST'
        try:
            if data:
                response = requests.post('%s%s' % (self._endpoint_url, url),
                                         data=json.dumps(data),
                                         headers=self.get_request_headers())
            else:
                response = requests.post('%s%s' % (self._endpoint_url, url),
                                         headers=self.get_request_headers())
        except Exception:
            raise RestUnreachableError(verb, url)

        self._check_response(verb, url, response)
        return response.json()

    def delete(self, url):
        verb = 'DELETE'
        try:
            response = requests.post('%s%s' % (self._endpoint_url, url),
                                         headers=self.get_request_headers())
        except Exception:
            raise RestUnreachableError(verb, url)

        self._check_response(verb, url, response)
        return response.json()

    @staticmethod
    def _check_response(verb, url, response):
        status_code = response.status_code
        if status_code < 200 or status_code > 299:
            try:
                response_body = response.json()
                if status_code == 422 and response_body.get('code', None):
                    if response_body.get('code', None) == 'ValidationError':
                        vr = ValidationResults(
                            response_body.get('validationResults', None))
                        error = ValidationError(verb, url, vr)
                    else:
                        error = ScannerError(verb,
                                             url,
                                             response_body.get('code', None),
                                             response_body.get('message', None))
                else:
                    error = RestError(verb,
                                      url,
                                      status_code,
                                      response_body.get('message', None))
            except Exception:
                error = RestError(verb, url, status_code)

            raise error

    # region "endpoint_url" accessors
    def _get_endpoint_url(self):
        return self._endpoint_url

    def _set_endpoint_url(self, value):
        if not value:
            raise Exception('The provided "endpoint_url" is not valid')
        self._endpoint_url = value

    endpoint_url = property(_get_endpoint_url, _set_endpoint_url)
    # endregion

    # region "api_key" accessors
    def _get_api_key(self):
        return self._api_key

    def _set_api_key(self, value):
        if not value:
            raise Exception('The provided "api_key" is not valid')
        self._api_key = value

    api_key = property(_get_api_key, _set_api_key)
    # endregion

    # region "custom_request_headers" accessors
    def _get_custom_request_headers(self):
        return self._custom_request_headers

    def _set_custom_request_headers(self, value):
        if not value:
            raise Exception('The provided "custom_request_headers" is not valid')
        self._custom_request_headers = value

    custom_request_headers = property(_get_custom_request_headers, _set_custom_request_headers)
    
    def add_custom_request_headers(self, key, value):
        if not key:
            raise Exception('The provided "field" is not valid')
        if not value:
            raise Exception('The provided "field value" is not valid')
        self._custom_request_headers[key] = value
        
    def remove_custom_request_headers(self, key):
        if key not in self._custom_request_headers:
            raise Exception('The provided "field" is not valid')
        del self._custom_request_headers[key]
    # endregion

    # region "multipart_upload_double_check" accessors
    def _get_multipart_upload_double_check(self):
        return self._multipart_upload_double_check

    def _set_multipart_upload_double_check(self, value):
        if not value:
            raise Exception(
                'The provided "multipart_upload_double_check" is '
                'not valid')
        self._multipart_upload_double_check = value
    multipart_upload_double_check = property(_get_multipart_upload_double_check, _set_multipart_upload_double_check)
    # endregion

    # region "multipart_upload_threshold" accessors
    def _get_multipart_upload_threshold(self):
        return self._multipart_upload_threshold

    def _set_multipart_upload_threshold(self, value):
        if not value:
            raise Exception(
                'The provided "multipart_upload_threshold" is not '
                'valid')
        self._multipart_upload_threshold = value
    multipart_upload_threshold = property(_get_multipart_upload_threshold, _set_multipart_upload_threshold)
    # endregion

__all__ = ['RestClient']
