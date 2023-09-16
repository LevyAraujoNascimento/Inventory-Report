from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report
from datetime import datetime, date


class SimpleReport(Report):
    def __init__(self) -> None:
        self._invetories: list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self._invetories.append(inventory)

    def largest_inventory(self) -> str:
        companies: dict[str, int] = {}

        for invent in self._invetories:
            for product in invent._data:
                comp_name = product.company_name
                if comp_name in companies:
                    companies[comp_name] += 1
                else:
                    companies[comp_name] = 1

        result = max(companies, key=companies.get)

        return result

    def generate(self) -> str:
        oldestDate = None
        closestDate = None
        largInvent = self.largest_inventory()

        today = date.today()

        for invent in self._invetories:
            for product in invent._data:
                manu = product.manufacturing_date
                exp = product.expiration_date
                dateManu = datetime.strptime(manu, '%Y-%m-%d').date()
                dateExp = datetime.strptime(exp, '%Y-%m-%d').date()

                if oldestDate is None or dateManu < oldestDate:
                    oldestDate = dateManu

                if dateExp >= today and (
                    closestDate is None
                    or dateExp < closestDate
                ):
                    closestDate = dateExp

        return (
            f"Oldest manufacturing date: {oldestDate}"
            f"Closest expiration date: {closestDate}"
            f"Company with the largest inventory: {largInvent}"
            )
