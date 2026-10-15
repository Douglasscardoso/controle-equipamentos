from emprestimo import Emprestimo
from equipamento import Equipamento


class ControleEquipamentos:
    """Gerencia o cadastro de equipamentos e seus empréstimos."""

    def __init__(self):
        self.equipamentos: dict[str, Equipamento] = {}
        self.emprestimos: list[Emprestimo] = []

    def cadastrar_equipamento(
        self, codigo: str, nome: str, quantidade: int
    ) -> Equipamento:
        codigo = codigo.strip()
        if codigo in self.equipamentos:
            raise ValueError(f"já existe um equipamento com o código {codigo}")

        equipamento = Equipamento(codigo, nome, quantidade)
        self.equipamentos[equipamento.codigo] = equipamento
        return equipamento

    def buscar_equipamento(self, codigo: str) -> Equipamento:
        try:
            return self.equipamentos[codigo.strip()]
        except KeyError:
            raise ValueError(f"equipamento {codigo} não encontrado") from None

    def emprestar(self, pessoa: str, codigo: str, quantidade: int) -> Emprestimo:
        """Registra um empréstimo e baixa o saldo do equipamento."""
        if not pessoa.strip():
            raise ValueError("informe o nome da pessoa")

        equipamento = self.buscar_equipamento(codigo)
        equipamento.emprestar(quantidade)

        emprestimo = Emprestimo(
            id=len(self.emprestimos) + 1,
            pessoa=pessoa.strip(),
            equipamento=equipamento,
            quantidade=quantidade,
        )
        self.emprestimos.append(emprestimo)
        return emprestimo

    def devolver(self, id_emprestimo: int) -> Emprestimo:
        """Registra a devolução de um empréstimo e repõe o saldo."""
        for emprestimo in self.emprestimos:
            if emprestimo.id == id_emprestimo:
                emprestimo.devolver()
                return emprestimo
        raise ValueError(f"empréstimo #{id_emprestimo} não encontrado")

    def emprestimos_em_aberto(self) -> list[Emprestimo]:
        return [e for e in self.emprestimos if not e.devolvido]
