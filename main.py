from controle import ControleEquipamentos


def main() -> None:
    controle = ControleEquipamentos()

    furadeira = controle.cadastrar_equipamento("001", "furadeira", 5)
    print(furadeira)

    emprestimo = controle.emprestar("Douglas", "001", 1)
    print(emprestimo)
    print(furadeira)

    controle.devolver(emprestimo.id)
    print(emprestimo)
    print(furadeira)


if __name__ == "__main__":
    main()
