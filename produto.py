class Produto:

    def __init__(self, codigo, nome, categoria, preco, fornecedor):

        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.fornecedor = fornecedor

    def __str__(self):

        return (f"Produto[codigo = {self.codigo}, nome = {self.nome}, "
            f"categoria = {self.categoria}, preco = {self.preco:.2f}, fornecedor = {self.fornecedor}]")

