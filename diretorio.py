class Diretorio:
    """
    Classe que implementa um diretório para indexar e buscar produtos por critérios.
    """

    def __init__(self, campo, tipo):
        """
        Inicializa um diretório para indexar produtos com base em um campo específico.

        :param campo: Nome do campo a ser indexado (ex.: 'categoria', 'preco', 'fornecedor').
        :param tipo: Tipo de dados do campo ('discreto' ou 'contínuo').
        """
        self.campo = campo
        self.tipo = tipo  # Tipo pode ser 'discreto' ou 'contínuo'
        self.indices = {}

    def indexar(self, produto):
        """
        Adiciona um produto ao índice com base no valor do campo.

        :param produto: Instância da classe Produto.
        """
        valor = getattr(produto, self.campo)
        if valor not in self.indices:
            self.indices[valor] = []
        self.indices[valor].append(produto.codigo)

    def buscar(self, valor):
        """
        Busca produtos que atendem a um critério no índice.

        :param valor: Valor do campo a ser buscado.
        :return: Lista de códigos dos produtos que atendem ao critério.
        """
        return self.indices.get(valor, [])

    def buscar_por_faixa(self, min_valor, max_valor):
        """
        Busca produtos cujos valores estão dentro de uma faixa (apenas para campos contínuos).

        :param min_valor: Valor mínimo da faixa.
        :param max_valor: Valor máximo da faixa.
        :return: Lista de códigos dos produtos que atendem ao critério de faixa.
        """
        if self.tipo != "contínuo":
            raise ValueError("Busca por faixa só está disponível para diretórios contínuos.")
        
        resultados = []
        for valor, codigos in self.indices.items():
            if min_valor <= valor <= max_valor:
                resultados.extend(codigos)
        return resultados

    def combinar_buscas(self, outro_diretorio, valor1, valor2):
        """
        Combina buscas de dois diretórios (interseção).

        :param outro_diretorio: Outro diretório para combinar a busca.
        :param valor1: Valor do campo deste diretório.
        :param valor2: Valor do campo do outro diretório.
        :return: Lista de códigos dos produtos que atendem a ambos os critérios.
        """
        resultados1 = set(self.buscar(valor1))
        resultados2 = set(outro_diretorio.buscar(valor2))
        return list(resultados1 & resultados2)

    def exibir_indices(self):
        """
        Exibe o índice completo para depuração.
        """
        return self.indices
    



