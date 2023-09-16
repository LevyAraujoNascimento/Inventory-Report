from inventory_report.product import Product
from abc import ABC, abstractmethod
from typing import Dict, Type
import json
import csv


class Importer(ABC):
    def __init__(self, path: str) -> None:
        pass

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def __init__(self, path: str) -> None:
        self.path = path

    def import_data(self) -> list[Product]:
        result = list()
        with open(self.path) as file:
            data = json.load(file)
        for element in data:
            result.append(Product(**element))
        return result


class CsvImporter(Importer):
    def __init__(self, path: str) -> None:
        self.path = path

    def import_data(self) -> list[Product]:
        result = list()
        with open(self.path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            for row in reader:
                result.append(Product(
                    id=row["id"],
                    product_name=row["product_name"],
                    company_name=row["company_name"],
                    manufacturing_date=row["manufacturing_date"],
                    expiration_date=row["expiration_date"],
                    serial_number=row["serial_number"],
                    storage_instructions=row["storage_instructions"],
                ))

        return result


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
