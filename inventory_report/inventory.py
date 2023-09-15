from typing import Optional
from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Optional[list[Product]] = None) -> None:
        if data is None:
            self._data: list[Product] = list()
        else:
            self._data = data

    def add_data(self, data: list[Product]) -> None:
        for element in data:
            self._data.append(element)

    @property
    def data(self) -> list[Product]:
        return self._data
