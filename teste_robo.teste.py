import unittest
from robo_de_limpeza import RoboDeLimpeza

class TestRoboDeLimpeza(unittest.TestCase):
    def setUp(self):
        self.robo = RoboDeLimpeza()

    def test_adicionar_tarefa(self):
        tarefa = "Limpar o banheiro"
        self.robo.adicionarTarefa(tarefa)
        self.assertEqual(self.robo.fila.ultimo(), tarefa)

    def test_executar_proxima_tarefa(self):
        tarefa = self.robo.executarProximaTarefa()
        self.assertEqual(tarefa, "Lavar o chão")

    def test_executar_todas_tarefas(self):
        tarefas = self.robo.executarTodasTarefas()
        self.assertEqual(tarefas, ["Lavar o chão", "Limpar as janelas", "Aspirar o tapete"])

if __name__ == '__main__':
    unittest.main()