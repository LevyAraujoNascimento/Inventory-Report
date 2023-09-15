from inventory_report.product import Product
from abc import ABC, abstractmethod
from typing import Dict, Type
import json


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


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
