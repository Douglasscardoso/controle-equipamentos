
from equipamento import Equipamento
from emprestimo import Emprestimo
emprestimos = []       



equipamento1 = Equipamento("001", "furadeira", 5)
print(f"codigo\t",equipamento1.codigo)
print("Equipamento\t",equipamento1.nome)
print("saldo disponivel\t",equipamento1.quantidade_disponivel)


emprestimo1 = Emprestimo("Douglas", equipamento1, 1)
print("usuario\t",emprestimo1.pessoa)
print("Equipamento\t",emprestimo1.equipamento.nome)
emprestimo1.registrar(emprestimos)
print("saldo disponivel",equipamento1.quantidade_disponivel)
print(emprestimos[0].pessoa)
print(emprestimos[0].equipamento.nome)
print(emprestimos[0].quantidade)





