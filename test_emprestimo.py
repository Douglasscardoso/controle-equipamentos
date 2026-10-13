import unittest

from emprestimo import Emprestimo
from equipamento import Equipamento


class TestEmprestimo(unittest.TestCase):
    def setUp(self):
        self.furadeira = Equipamento("001", "furadeira", 5)
        self.emprestimos = []

    def test_registrar_com_sucesso(self):
        emprestimo = Emprestimo("Douglas", self.furadeira, 1)
        self.assertTrue(emprestimo.registrar(self.emprestimos))
        self.assertEqual(self.emprestimos, [emprestimo])
        self.assertEqual(self.furadeira.quantidade_disponivel, 4)

    def test_registrar_falha_nao_altera_nada(self):
        emprestimo = Emprestimo("Douglas", self.furadeira, 10)
        self.assertFalse(emprestimo.registrar(self.emprestimos))
        self.assertEqual(self.emprestimos, [])
        self.assertEqual(self.furadeira.quantidade_disponivel, 5)

    def test_devolver(self):
        emprestimo = Emprestimo("Douglas", self.furadeira, 2)
        emprestimo.registrar(self.emprestimos)
        emprestimo.devolver()
        self.assertTrue(emprestimo.devolvido)
        self.assertEqual(self.furadeira.quantidade_disponivel, 5)

    def test_devolver_duas_vezes(self):
        emprestimo = Emprestimo("Douglas", self.furadeira, 2)
        emprestimo.registrar(self.emprestimos)
        emprestimo.devolver()
        with self.assertRaises(ValueError):
            emprestimo.devolver()


if __name__ == "__main__":
    unittest.main()
