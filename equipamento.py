class Equipamento:
    """Equipamento com controle de saldo disponível para empréstimo."""

    def __init__(self, codigo: str, nome: str, quantidade_total: int):
        self.codigo = codigo
        self.nome = nome
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
