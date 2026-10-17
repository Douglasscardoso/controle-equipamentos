import unittest

from controle_equipamentos import ControleEquipamentos


class TestControleEquipamentos(unittest.TestCase):
    def setUp(self):
        self.controle = ControleEquipamentos()
        self.furadeira = self.controle.cadastrar_equipamento("001", "furadeira", 5)

    def test_codigo_duplicado(self):
        with self.assertRaises(ValueError):
            self.controle.cadastrar_equipamento("001", "outra", 1)

    def test_emprestar_com_sucesso(self):
        emprestimo = self.controle.emprestar("Douglas", "001", 1)
        self.assertEqual(emprestimo.id, 1)
        self.assertEqual(self.furadeira.quantidade_disponivel, 4)
        self.assertEqual(self.controle.emprestimos_em_aberto(), [emprestimo])

    def test_emprestar_falha_nao_altera_nada(self):
        with self.assertRaises(ValueError):
            self.controle.emprestar("Douglas", "001", 10)
        self.assertEqual(self.furadeira.quantidade_disponivel, 5)
        self.assertEqual(self.controle.emprestimos, [])

    def test_emprestar_equipamento_inexistente(self):
        with self.assertRaises(ValueError):
            self.controle.emprestar("Douglas", "999", 1)

    def test_emprestar_sem_nome(self):
        with self.assertRaises(ValueError):
            self.controle.emprestar("  ", "001", 1)

    def test_devolver(self):
        emprestimo = self.controle.emprestar("Douglas", "001", 2)
        self.controle.devolver(emprestimo.id)
        self.assertTrue(emprestimo.devolvido)
        self.assertEqual(self.furadeira.quantidade_disponivel, 5)
        self.assertEqual(self.controle.emprestimos_em_aberto(), [])

    def test_devolver_duas_vezes(self):
        emprestimo = self.controle.emprestar("Douglas", "001", 2)
        self.controle.devolver(emprestimo.id)
        with self.assertRaises(ValueError):
            self.controle.devolver(emprestimo.id)
        self.assertEqual(self.furadeira.quantidade_disponivel, 5)

    def test_devolver_emprestimo_inexistente(self):
        with self.assertRaises(ValueError):
            self.controle.devolver(42)


if __name__ == "__main__":
    unittest.main()
