class Equipamento:
    def __init__(self, codigo, nome, quantidade_total):
        self.codigo = codigo
        self.nome = nome
        self.quantidade_total = quantidade_total
        self.quantidade_disponivel = self.quantidade_total

    def emprestar(self, quantidade):
        if quantidade > self.quantidade_disponivel:
            return "quantidade maior que a disponivel"
        elif quantidade <= 0:
            return "quantidade invalida"
        else:
            self.quantidade_disponivel = self.quantidade_disponivel - quantidade
            return self.quantidade_disponivel