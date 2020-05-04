class DescriptiveMetadata:
    def __init__(self, model):
        self.title = model["title"]
        self.keywords = model["keywords"]
        self.creator = model["creator"]
        self.date_created = model["dateCreated"]
        self.location_created = model["locationCreated"]
        self.classification = model["classification"]
        self.document_type = model["documentType"]
        self.destination = model["destination"]
        self.genre = model["genre"]
        self.storage_period = model["storagePeriod"]

__all__ = ['DescriptiveMetadata']