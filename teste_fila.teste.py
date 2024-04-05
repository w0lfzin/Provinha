import unittest
from Fila import Fila

class TestFila(unittest.TestCase):

    def setUp(self):
        self.fila = Fila()

    def test_adicionar_e_remover(self):
        self.fila.adicionar('Tarefa 1')
        self.assertEqual(self.fila.remover(), 'Tarefa 1')

    def test_remover_de_fila_vazia(self):
        with self.assertRaises(Exception) as context:
            self.fila.remover()
        self.assertTrue('A fila de tarefas está vazia.' in str(context.exception))

    def test_fila_vazia(self):
        self.assertTrue(self.fila.vazia())
        self.fila.adicionar('Tarefa 1')
        self.assertFalse(self.fila.vazia())

if __name__ == "__main__":
    unittest.main()