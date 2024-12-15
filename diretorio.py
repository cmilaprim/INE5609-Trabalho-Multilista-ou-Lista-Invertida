class Diretorio:
    def __init__(self, campo, tipo):
        self.campo = campo
        self.tipo = tipo 
        self.indices = {}

    def indexar(self, produto):
        valor = getattr(produto, self.campo)
        if valor not in self.indices:
            self.indices[valor] = []
        self.indices[valor].append(produto.codigo)

    def buscar(self, valor):
        return self.indices.get(valor, [])

    def buscar_por_faixa(self, min_valor, max_valor):
        if self.tipo != "contínuo":
            raise ValueError("Busca por faixa só está disponível para diretórios contínuos.")
        
        resultados = []
        for valor, codigos in self.indices.items():
            if min_valor <= valor <= max_valor:
                resultados.extend(codigos)
        return resultados

    def combinar_buscas(self, outro_diretorio, valor1, valor2):
        resultados1 = set(self.buscar(valor1))
        resultados2 = set(outro_diretorio.buscar(valor2))
        return list(resultados1 & resultados2)

    def exibir_indices(self):
        return self.indices
    



