class Equipamento:
    """Equipamento com controle de saldo disponível para empréstimo."""

    def __init__(self, codigo: str, nome: str, quantidade_total: int):
        if not codigo.strip() or not nome.strip():
            raise ValueError("código e nome são obrigatórios")
        if quantidade_total <= 0:
            raise ValueError("quantidade total deve ser maior que zero")

        self.codigo = codigo.strip()
        self.nome = nome.strip()
        self.quantidade_total = quantidade_total
        self.quantidade_disponivel = quantidade_total

    def emprestar(self, quantidade: int) -> int:
        """Retira `quantidade` do saldo e devolve o novo saldo disponível."""
        if quantidade <= 0:
            raise ValueError("quantidade inválida")
        if quantidade > self.quantidade_disponivel:
            raise ValueError("quantidade maior que a disponível")

        self.quantidade_disponivel -= quantidade
        return self.quantidade_disponivel

    def devolver(self, quantidade: int) -> int:
        """Devolve `quantidade` ao saldo e retorna o novo saldo disponível."""
        if quantidade <= 0:
            raise ValueError("quantidade inválida")
        if self.quantidade_disponivel + quantidade > self.quantidade_total:
            raise ValueError("devolução maior que a quantidade emprestada")

        self.quantidade_disponivel += quantidade
        return self.quantidade_disponivel

    def __str__(self) -> str:
        return (
            f"[{self.codigo}] {self.nome} - "
            f"{self.quantidade_disponivel}/{self.quantidade_total} disponíveis"
        )
