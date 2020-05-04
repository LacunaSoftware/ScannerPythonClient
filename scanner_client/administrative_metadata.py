class AdministrativeMetadata:
    def __init__(self, model):
        self.scanned_by_domestic_government = model["scannedByDomesticGovernment"]
        self.scanning_person_name = model["scanningPersonName"]
        self.scanning_person_cpf = model["scanningPersonCpf"]
        self.scanning_entity_name = model["scanningEntityName"]
        self.scanning_entity_cnpj = model["scanningEntityCnpj"]
        self.date_scanned = model["dateScanned"]
        self.location_scanned = model["locationScanned"]

__all__ = ['AdministrativeMetadata']