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
        companies = self.companies_stock()
        report = super().generate()

        final_report = f"{report}\nStocked products by company:\n"

        for company, quant in companies.items():
            final_report += f"- {company}: {quant}\n"

        return final_report
