from datetime import datetime, date
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def companies_stock(self) -> dict[str, int]:
        companies: dict[str, int] = {}

        for invent in self._invetories:
            for product in invent._data:
                comp_name = product.company_name
                if comp_name in companies:
                    companies[comp_name] += 1
                else:
                    companies[comp_name] = 1

        return companies

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

        result = (
            f"Oldest manufacturing date: {oldestDate}\n"
            f"Closest expiration date: {closestDate}\n"
            f"Company with the largest inventory: {largInvent}\n"
            f"Stocked products by company:\n"
        )

        companies = self.companies_stock()

        for name, count in companies.items():
            result += f"- {name}: {count}\n"

        return result
