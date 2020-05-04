import base64
import binascii

from six import BytesIO


def _base64_decode(value):
    if value is None:
        raise Exception('The provided value is not valid')
    try:
        raw = base64.standard_b64decode(value)
    except (TypeError, binascii.Error):
        raise Exception('The provided certificate is not Base64-encoded')
    return raw
