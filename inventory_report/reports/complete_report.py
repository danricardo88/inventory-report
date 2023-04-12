from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        oldest_date = min(item["data_de_fabricacao"] for item in data)
        nearest_date = min(item["data_de_validade"] for item in data)
        largest_stock = max(
            (item["nome_da_empresa"], data.count(item)) for item in set(data)
        )
        stock_per_company = {}
        for item in data:
            stock_per_company[item["nome_da_empresa"]] = (
                stock_per_company.get(item["nome_da_empresa"], 0) + 1
            )
        stock_per_company = sorted(
            stock_per_company.items(),
            key=lambda x: data.index({"nome_da_empresa": x[0]}),
        )

        result = f"Data de fabricação mais antiga: {oldest_date}\n"
        result += f"Data de validade mais próxima: {nearest_date}\n"
        result += f"Empresa com mais produtos: {largest_stock[0]}\n"
        result += "Produtos estocados por empresa:\n"
        for company, stock in stock_per_company:
            result += f"- {company}: {stock}\n"

        return result
