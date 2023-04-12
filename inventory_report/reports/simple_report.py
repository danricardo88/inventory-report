from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(products):
        data_fabricacao_antiga = min(
            datetime.strptime(p["data_de_fabricacao"], "%Y-%m-%d")
            for p in products
        ).strftime("%Y-%m-%d")

        validade_proxima = min(
            datetime.strptime(p["data_de_validade"], "%Y-%m-%d")
            for p in products
            if datetime.strptime(p["data_de_validade"], "%Y-%m-%d")
            >= datetime.today()
        ).strftime("%Y-%m-%d")

        empresas = [p["nome_da_empresa"] for p in products]
        empresa_mais_produtos = max(empresas, key=empresas.count)

        return (
            f"Data de fabricação mais antiga: {data_fabricacao_antiga}\n"
            f"Data de validade mais próxima: {validade_proxima}\n"
            f"Empresa com mais produtos: {empresa_mais_produtos}\n"
        )
