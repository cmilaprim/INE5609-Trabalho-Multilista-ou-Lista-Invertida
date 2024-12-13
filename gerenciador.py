
from base_de_dados import BaseDeDados
from diretorio import Diretorio
from produto import Produto

class GerenciadorDeEstoque:
    """
    Classe que gerencia o estoque e centraliza as operações do sistema.
    """
    def __init__(self):
        """
        Inicializa o gerenciador de estoque.
        """
        # Instancia a base de dados
        self.base_de_dados = BaseDeDados()

        # Cria diretórios para indexação
        self.diretorio_categoria = Diretorio(campo="categoria", tipo="discreto")
        self.diretorio_fornecedor = Diretorio(campo="fornecedor", tipo="discreto")
        self.diretorio_preco = Diretorio(campo="preco", tipo="contínuo")

    def carregar_produtos_iniciais(self, produtos):
        """
        Carrega produtos iniciais na base de dados e os indexa nos diretórios.

        :param produtos: Lista de instâncias da classe Produto.
        """
        for produto in produtos:
            self.base_de_dados.inserir_produto(produto)
            self.indexar_produto(produto)

    def indexar_produto(self, produto):
        """
        Indexa um produto nos diretórios.

        :param produto: Instância da classe Produto.
        """
        self.diretorio_categoria.indexar(produto)
        self.diretorio_fornecedor.indexar(produto)
        self.diretorio_preco.indexar(produto)

    def adicionar_produto(self, codigo, nome, categoria, preco, fornecedor):
        """
        Adiciona um novo produto ao sistema.

        :param codigo: Código do produto.
        :param nome: Nome do produto.
        :param categoria: Categoria do produto.
        :param preco: Preço do produto.
        :param fornecedor: Fornecedor do produto.
        """
        produto = Produto(codigo, nome, categoria, preco, fornecedor)
        self.base_de_dados.inserir_produto(produto)
        self.indexar_produto(produto)

    def buscar_produto_por_codigo(self, codigo):
        """
        Busca um produto pelo código único.

        :param codigo: Código do produto a ser buscado.
        :return: Produto encontrado ou None.
        """
        return self.base_de_dados.buscar_por_codigo(codigo)

    def excluir_produto_por_codigo(self, codigo):

        produto = self.base_de_dados.excluir_por_codigo(codigo)
        return produto

    def listar_todos_produtos(self):
        """
        Lista todos os produtos cadastrados no sistema.

        :return: Lista de produtos.
        """
        return self.base_de_dados.listar_todos()

    def consultar_por_categoria(self, categoria):
        """
        Consulta produtos por categoria.

        :param categoria: Categoria a ser buscada.
        :return: Lista de códigos de produtos na categoria.
        """
        return self.diretorio_categoria.buscar(categoria)

    def consultar_por_fornecedor(self, fornecedor):
        """
        Consulta produtos por fornecedor.

        :param fornecedor: Fornecedor a ser buscado.
        :return: Lista de códigos de produtos fornecidos pelo fornecedor.
        """
        return self.diretorio_fornecedor.buscar(fornecedor)

    def consultar_por_preco(self, preco):
        """
        Consulta produtos por preço.

        :param preco: Preço a ser buscado.
        :return: Lista de códigos de produtos com o preço informado.
        """
        return self.diretorio_preco.buscar(preco)
    
    def consultar_por_faixa_de_preco(self, min_preco, max_preco):
        """
        Consulta produtos dentro de uma faixa de preço (apenas para campos contínuos).

        :param min_preco: Preço mínimo da faixa.
        :param max_preco: Preço máximo da faixa.
        """
        codigos = self.diretorio_preco.buscar_por_faixa(min_preco, max_preco)
        return self.exibir_produtos(codigos)
    
    def consulta_combinada(self, categoria=None, fornecedor=None, faixa_preco=None):
        # Inicializa os resultados como todos os produtos (base inicial)
        resultados = set(self.base_de_dados.produtos.keys())

        # Filtro por categoria
        if categoria:
            codigos_categoria = set(self.diretorio_categoria.buscar(categoria))
            resultados &= codigos_categoria

        # Filtro por fornecedor
        if fornecedor:
            codigos_fornecedor = set(self.diretorio_fornecedor.buscar(fornecedor))
            resultados &= codigos_fornecedor

        # Filtro por faixa de preço
        if faixa_preco:
            min_preco, max_preco = faixa_preco
            codigos_faixa_preco = set(self.diretorio_preco.buscar_por_faixa(min_preco, max_preco))
            resultados &= codigos_faixa_preco

        # Retorna os resultados como lista
        return list(resultados)


    def exibir_produtos(self, codigos):
        """
        Exibe as informações dos produtos encontrados.

        :param codigos: Lista de códigos dos produtos encontrados.
        """
        if not codigos:
            print("Nenhum produto encontrado.")
            return

        for codigo in codigos:
            produto = self.buscar_produto_por_codigo(codigo)
            if produto:
                print(produto)
            else:
                print(f"Produto com código {codigo} não encontrado.")


# Programa principal
if __name__ == "__main__":
    # Instancia o gerenciador de estoque
    gerenciador = GerenciadorDeEstoque()

    # Cria produtos iniciais
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
        Produto("P011", "Notebook", "Eletrônicos", 900.00, "Fornecedor C"),  # Adicionado para consulta combinada
    ]

    # Carrega os produtos iniciais no gerenciador
    gerenciador.carregar_produtos_iniciais(produtos_iniciais)

    # Exibe todos os produtos inicialmente
    print("\n=== Lista de Todos os Produtos ===")
    todos_produtos = gerenciador.listar_todos_produtos()
    gerenciador.exibir_produtos([produto.codigo for produto in todos_produtos])

    # Adicionar um novo produto
    print("\n=== Adicionando Novo Produto ===")
    gerenciador.adicionar_produto("P012", "Agenda 2024", "Papelaria", 20.00, "Fornecedor B")
    print("Novo produto adicionado. Lista de produtos atualizada:")
    todos_produtos = gerenciador.listar_todos_produtos()
    gerenciador.exibir_produtos([produto.codigo for produto in todos_produtos])

    # Buscar produto pelo código
    print("\n=== Busca por Código ===")
    codigo_busca = "P003"
    produto = gerenciador.buscar_produto_por_codigo(codigo_busca)
    if produto:
        gerenciador.exibir_produtos([produto.codigo])
    else:
        print(f"Produto com código {codigo_busca} não encontrado.")

    # Consulta por categoria
    print("\n=== Consulta por Categoria 'Papelaria' ===")
    codigos_categoria = gerenciador.consultar_por_categoria("Papelaria")
    gerenciador.exibir_produtos(codigos_categoria)

    # Consulta por fornecedor
    print("\n=== Consulta por Fornecedor 'Fornecedor C' ===")
    codigos_fornecedor = gerenciador.consultar_por_fornecedor("Fornecedor C")
    gerenciador.exibir_produtos(codigos_fornecedor)

    # Consulta por faixa de preço
    print("\n=== Consulta por Faixa de Preço entre 10 e 50 ===")
    gerenciador.consultar_por_faixa_de_preco(10, 50)

    # Consulta combinada: Categoria x Fornecedor x Faixa de Preço
    print("\n=== Consulta Combinada: Categoria 'Eletrônicos', Fornecedor 'Fornecedor C', Faixa de Preço (800, 1000) ===")
    codigos_combinados = gerenciador.consulta_combinada(categoria="Eletrônicos", fornecedor="Fornecedor C", faixa_preco=(800, 1000))
    gerenciador.exibir_produtos(codigos_combinados)

    # Excluir um produto pelo código
    print("\n=== Excluindo Produto com Código 'P004' ===")
    produto_removido = gerenciador.excluir_produto_por_codigo("P004")
    if produto_removido:
        gerenciador.exibir_produtos([produto_removido.codigo])
    else:
        print("Produto não encontrado para remoção.")

    # Exibe a lista final de produtos
    print("\n=== Lista Final de Produtos ===")
    todos_produtos = gerenciador.listar_todos_produtos()
    gerenciador.exibir_produtos([produto.codigo for produto in todos_produtos])

