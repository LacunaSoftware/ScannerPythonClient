from .rest_base_error import RestBaseError


class ScannerError(RestBaseError):
    def __init__(self, verb, url, error_code, error_message):
        message = "Scanner API error %s" % (error_code)

        if error_message and len(error_message) > 0:
            message += ": %s" % error_message

        RestBaseError.__init__(self, __name__, message, verb, url)

        self.error_code = error_code
        self.error_message = error_message

__all__ = ['ScannerError']
