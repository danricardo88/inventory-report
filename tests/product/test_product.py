from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "Cai no golpe",
        "Não vale 40k",
        "2022-01-01",
        "2022-12-31",
        "12345",
        "Armazenar em local seco e fresco",
    )

    assert produto.id == 1
    assert produto.nome_da_empresa == "Não vale 40k"
    assert produto.nome_do_produto == "Cai no golpe"
    assert produto.data_de_fabricacao == "2022-01-01"
    assert produto.data_de_validade == "2022-12-31"
    assert produto.numero_de_serie == "12345"
    assert (
        produto.instrucoes_de_armazenamento
        == "Armazenar em local seco e fresco"
    )
