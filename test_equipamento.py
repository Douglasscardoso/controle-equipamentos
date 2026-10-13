import unittest

from equipamento import Equipamento


class TestEquipamento(unittest.TestCase):
    def setUp(self):
        self.furadeira = Equipamento("001", "furadeira", 5)

    def test_saldo_inicial_igual_ao_total(self):
        self.assertEqual(self.furadeira.quantidade_disponivel, 5)

    def test_emprestar_baixa_o_saldo(self):
        self.assertEqual(self.furadeira.emprestar(2), 3)

    def test_emprestar_todo_o_saldo(self):
        self.assertEqual(self.furadeira.emprestar(5), 0)

    def test_emprestar_maior_que_disponivel(self):
        with self.assertRaises(ValueError):
            self.furadeira.emprestar(6)
        self.assertEqual(self.furadeira.quantidade_disponivel, 5)

    def test_emprestar_quantidade_invalida(self):
        for quantidade in (0, -1):
            with self.assertRaises(ValueError):
                self.furadeira.emprestar(quantidade)

    def test_devolver_repoe_o_saldo(self):
        self.furadeira.emprestar(3)
        self.assertEqual(self.furadeira.devolver(2), 4)

    def test_devolver_mais_do_que_o_total(self):
        with self.assertRaises(ValueError):
            self.furadeira.devolver(1)


if __name__ == "__main__":
    unittest.main()
