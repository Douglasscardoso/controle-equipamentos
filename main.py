
class Equipamento:
    def __init__(self, codigo, nome, quantidade_total):
        self.codigo = codigo
        self.nome = nome
        self.quantidade_total = quantidade_total
        self.quantidade_disponivel = self.quantidade_total