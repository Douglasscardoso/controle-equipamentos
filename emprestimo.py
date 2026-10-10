from equipamento import Equipamento


class Emprestimo:
    """Empréstimo de uma quantidade de um equipamento para uma pessoa."""

    def __init__(self, pessoa: str, equipamento: Equipamento, quantidade: int):
        self.pessoa = pessoa
        self.equipamento = equipamento
        self.quantidade = quantidade

    def registrar(self, emprestimos: list) -> bool:
        """Baixa o saldo do equipamento e guarda o empréstimo em `emprestimos`.

        Retorna True se registrou, False se não foi possível.
        """
        try:
            self.equipamento.emprestar(self.quantidade)
        except ValueError as erro:
            print("não foi possível registrar")
            print(erro)
            return False

        print("registrado")
        emprestimos.append(self)
        return True
