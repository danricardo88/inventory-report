from inventory_report.inventory.product import Product


def test_relatorio_produto():
    pass  # Seu teste deve ser escrito aqui
    product = Product(
        1,
        "Nascido em",
        "Utero", "2020-01-01",
        "humano",
        "021",
        "em colo de mamãe"
    )

    assert str(product) == (
        "O produto Nascido em"
        " fabricado em 2020-01-01"
        " por Utero com validade"
        " até humano"
        " precisa ser armazenado em colo de mamãe."
    )
