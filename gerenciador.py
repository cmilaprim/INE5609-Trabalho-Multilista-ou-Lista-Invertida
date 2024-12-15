from base_de_dados import BaseDeDados
from diretorio import Diretorio
from produto import Produto

class GerenciadorDeEstoque:
    def __init__(self):
        self.base_de_dados = BaseDeDados()
        self.diretorio_categoria = Diretorio(campo="categoria", tipo="discreto")
        self.diretorio_fornecedor = Diretorio(campo="fornecedor", tipo="discreto")
        self.diretorio_preco = Diretorio(campo="preco", tipo="contínuo")

    def carregar_produtos_iniciais(self, produtos):
        for produto in produtos:
            self.base_de_dados.inserir_produto(produto)
            self.indexar_produto(produto)

    def indexar_produto(self, produto):
        self.diretorio_categoria.indexar(produto)
        self.diretorio_fornecedor.indexar(produto)
        self.diretorio_preco.indexar(produto)

    def adicionar_produto(self, codigo, nome, categoria, preco, fornecedor):
        produto = Produto(codigo, nome, categoria, preco, fornecedor)
        self.base_de_dados.inserir_produto(produto)
        self.indexar_produto(produto)

    def buscar_produto_por_codigo(self, codigo):
        return self.base_de_dados.buscar_por_codigo(codigo)

    def excluir_produto_por_codigo(self, codigo):
        produto = self.base_de_dados.excluir_por_codigo(codigo)
        return produto

    def listar_todos_produtos(self):
        return self.base_de_dados.listar_todos()

    def consultar_por_categoria(self, categoria):
        return self.diretorio_categoria.buscar(categoria)

    def consultar_por_fornecedor(self, fornecedor):
        return self.diretorio_fornecedor.buscar(fornecedor)

    def consultar_por_preco(self, preco):
        return self.diretorio_preco.buscar(preco)
    
    def consultar_por_faixa_de_preco(self, min_preco, max_preco):
        codigos = self.diretorio_preco.buscar_por_faixa(min_preco, max_preco)
        return self.exibir_produtos(codigos)
    
    def consulta_combinada(self, categoria=None, fornecedor=None, faixa_preco=None):
        resultados = set(self.base_de_dados.produtos.keys())
        if categoria:
            codigos_categoria = set(self.diretorio_categoria.buscar(categoria))
            resultados &= codigos_categoria

        if fornecedor:
            codigos_fornecedor = set(self.diretorio_fornecedor.buscar(fornecedor))
            resultados &= codigos_fornecedor

        if faixa_preco:
            min_preco, max_preco = faixa_preco
            codigos_faixa_preco = set(self.diretorio_preco.buscar_por_faixa(min_preco, max_preco))
            resultados &= codigos_faixa_preco

        return list(resultados)

    def exibir_produtos(self, codigos):
        if not codigos:
            print("Nenhum produto encontrado.")
            return

        for codigo in codigos:
            produto = self.buscar_produto_por_codigo(codigo)
            if produto:
                print(produto)
            else:
                print(f"Produto com código {codigo} não encontrado.")
