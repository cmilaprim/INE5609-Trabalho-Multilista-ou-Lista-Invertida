from produto import Produto

class BaseDeDados:

    def __init__(self):

        self.produtos = {}

    def inserir_produto(self, produto):

        if produto.codigo in self.produtos:
            raise ValueError(f"Produto com código {produto.codigo} já existe.")
        self.produtos[produto.codigo] = produto

    def buscar_por_codigo(self, codigo):

        return self.produtos.get(codigo, None)

    def excluir_por_codigo(self, codigo):

        return self.produtos.pop(codigo, None)

    def listar_todos(self):

        return list(self.produtos.values())
