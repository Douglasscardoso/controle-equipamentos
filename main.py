
class Equipamento:
    def __init__(self, codigo, nome, quantidade_total):
        self.codigo = codigo
        self.nome = nome
        self.quantidade_total = quantidade_total
        self.quantidade_disponivel = self.quantidade_total

equipamento1 = Equipamento("001", "furadeira", 2)
print(equipamento1.codigo)
print(equipamento1.nome)
print(equipamento1.quantidade_total)
print(equipamento1.quantidade_disponivel)




