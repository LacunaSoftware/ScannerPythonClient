class CreateScanSessionResponse:
    def __init__(self, model):
        self.scan_session_id = model["scanSessionId"]
        self.redirect_url = model["redirectUrl"]

__all__ = ['CreateScanSessionResponse']