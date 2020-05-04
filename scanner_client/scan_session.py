from .document import Document


class ScanSession:
    def __init__(self, client, model):
        self.client = client
        self.id = model["id"]
        self.multifile = model["multifile"]
        self.result = model["result"]
        self.documents = list(map(lambda d: Document(self.client, d) , model["documents"]))

__all__ = ['ScanSession']