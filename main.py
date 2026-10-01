
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
class Emprestimo:
    def __init__(self, pessoa, equipamento, quantidade):
        self.pessoa = pessoa 
        self.equipamento = equipamento
        self.quantidade = quantidade

        



equipamento1 = Equipamento("001", "furadeira", 2)
print(equipamento1.codigo)
print(equipamento1.nome)
print(equipamento1.quantidade_total)
print(equipamento1.quantidade_disponivel)
print(equipamento1.emprestar(1))
print(equipamento1.emprestar(2))

emprestimo1 = Emprestimo("Douglas", equipamento1, 2)
print(emprestimo1.pessoa)
print(emprestimo1.equipamento.nome)
print(emprestimo1.equipamento.emprestar(emprestimo1.quantidade))




