from produto import Produto
from gerenciador import GerenciadorDeEstoque

if __name__ == "__main__":
    gerenciador = GerenciadorDeEstoque()

    produtos_iniciais = [
        Produto("P001", "Caneta Azul", "Papelaria", 1.50, "Fornecedor A"),
        Produto("P002", "Caderno", "Papelaria", 15.00, "Fornecedor B"),
        Produto("P003", "Laptop", "Eletrônicos", 3500.00, "Fornecedor D"),
        Produto("P004", "Borracha", "Papelaria", 0.75, "Fornecedor A"),
        Produto("P005", "Cabo HDMI", "Acessórios", 25.00, "Fornecedor C"),
        Produto("P006", "Mouse", "Acessórios", 35.00, "Fornecedor C"),
        Produto("P007", "Monitor", "Eletrônicos", 700.00, "Fornecedor D"),
        Produto("P008", "Tesoura", "Papelaria", 5.00, "Fornecedor B"),
        Produto("P009", "Carregador", "Eletrônicos", 50.00, "Fornecedor C"),
        Produto("P010", "Teclado", "Acessórios", 120.00, "Fornecedor D"),
        Produto("P011", "Notebook", "Eletrônicos", 900.00, "Fornecedor C"),
    ]

    gerenciador.carregar_produtos_iniciais(produtos_iniciais)

    print("\n=== Lista de Todos os Produtos ===")
    todos_produtos = gerenciador.listar_todos_produtos()
    gerenciador.exibir_produtos([produto.codigo for produto in todos_produtos])

    print("\n=== Adicionando Novo Produto ===")
    gerenciador.adicionar_produto("P012", "Agenda 2024", "Papelaria", 20.00, "Fornecedor B")
    print("Novo produto adicionado. Lista de produtos atualizada:")
    todos_produtos = gerenciador.listar_todos_produtos()
    gerenciador.exibir_produtos([produto.codigo for produto in todos_produtos])

    print("\n=== Busca por Código ===")
    codigo_busca = "P003"
    produto = gerenciador.buscar_produto_por_codigo(codigo_busca)
    if produto:
        gerenciador.exibir_produtos([produto.codigo])
    else:
        print(f"Produto com código {codigo_busca} não encontrado.")

    print("\n=== Consulta por Categoria 'Papelaria' ===")
    codigos_categoria = gerenciador.consultar_por_categoria("Papelaria")
    gerenciador.exibir_produtos(codigos_categoria)

    print("\n=== Consulta por Fornecedor 'Fornecedor C' ===")
    codigos_fornecedor = gerenciador.consultar_por_fornecedor("Fornecedor C")
    gerenciador.exibir_produtos(codigos_fornecedor)

    print("\n=== Consulta por Faixa de Preço entre 10 e 50 ===")
    gerenciador.consultar_por_faixa_de_preco(10, 50)

    print("\n=== Consulta Combinada: Categoria 'Eletrônicos', Fornecedor 'Fornecedor C', Faixa de Preço (800, 1000) ===")
    codigos_combinados = gerenciador.consulta_combinada(categoria="Eletrônicos", fornecedor="Fornecedor C", faixa_preco=(800, 1000))
    gerenciador.exibir_produtos(codigos_combinados)

    print("\n=== Excluindo Produto com Código 'P004' ===")
    produto_removido = gerenciador.excluir_produto_por_codigo("P004")
    if produto_removido:
        gerenciador.exibir_produtos([produto_removido.codigo])
    else:
        print("Produto não encontrado para remoção.")

    print("\n=== Lista Final de Produtos ===")
    todos_produtos = gerenciador.listar_todos_produtos()
    gerenciador.exibir_produtos([produto.codigo for produto in todos_produtos])

