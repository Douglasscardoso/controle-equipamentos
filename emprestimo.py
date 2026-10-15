from dataclasses import dataclass, field
from datetime import datetime

from equipamento import Equipamento


@dataclass
class Emprestimo:
    """Empréstimo de uma quantidade de um equipamento para uma pessoa."""

    id: int
    pessoa: str
    equipamento: Equipamento
    quantidade: int
    data: datetime = field(default_factory=datetime.now)
    devolvido: bool = False

    def devolver(self) -> None:
        """Devolve o equipamento ao saldo e marca o empréstimo como encerrado."""
        if self.devolvido:
            raise ValueError("este empréstimo já foi devolvido")

        self.equipamento.devolver(self.quantidade)
        self.devolvido = True

    def __str__(self) -> str:
        situacao = "devolvido" if self.devolvido else "em aberto"
        return (
            f"#{self.id} {self.pessoa} - {self.quantidade}x {self.equipamento.nome} "
            f"({self.data:%d/%m/%Y %H:%M}, {situacao})"
        )
