from controle_equipamentos.controle import ControleEquipamentos

MENU = """
=== Controle de Equipamentos ===
1 - Cadastrar equipamento
2 - Listar equipamentos
3 - Registrar empréstimo
4 - Registrar devolução
5 - Listar empréstimos em aberto
0 - Sair
"""


def ler_inteiro(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro.")


def cadastrar(controle: ControleEquipamentos) -> None:
    codigo = input("Código: ")
    nome = input("Nome: ")
    quantidade = ler_inteiro("Quantidade: ")
    equipamento = controle.cadastrar_equipamento(codigo, nome, quantidade)
    print(f"Cadastrado: {equipamento}")


def listar_equipamentos(controle: ControleEquipamentos) -> None:
    if not controle.equipamentos:
        print("Nenhum equipamento cadastrado.")
    for equipamento in controle.equipamentos.values():
        print(equipamento)


def emprestar(controle: ControleEquipamentos) -> None:
    pessoa = input("Pessoa: ")
    codigo = input("Código do equipamento: ")
    quantidade = ler_inteiro("Quantidade: ")
    emprestimo = controle.emprestar(pessoa, codigo, quantidade)
    print(f"Registrado: {emprestimo}")


def devolver(controle: ControleEquipamentos) -> None:
    id_emprestimo = ler_inteiro("Número do empréstimo: ")
    emprestimo = controle.devolver(id_emprestimo)
    print(f"Devolvido: {emprestimo}")


def listar_emprestimos(controle: ControleEquipamentos) -> None:
    em_aberto = controle.emprestimos_em_aberto()
    if not em_aberto:
        print("Nenhum empréstimo em aberto.")
    for emprestimo in em_aberto:
        print(emprestimo)


ACOES = {
    "1": cadastrar,
    "2": listar_equipamentos,
    "3": emprestar,
    "4": devolver,
    "5": listar_emprestimos,
}


def main() -> None:
    controle = ControleEquipamentos()
    controle.cadastrar_equipamento("001", "furadeira", 5)

    while True:
        print(MENU)
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "0":
            print("Até logo!")
            break

        acao = ACOES.get(opcao)
        if acao is None:
            print("Opção inválida.")
            continue

        try:
            acao(controle)
        except ValueError as erro:
            print(f"Erro: {erro}")
