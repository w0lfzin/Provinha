from Fila import Fila

class RoboDeLimpeza:
    def __init__(self):
        self.fila = Fila()
        self.fila.adicionar("Lavar o chão")
        self.fila.adicionar("Limpar as janelas")
        self.fila.adicionar("Aspirar o tapete")

    def adicionarTarefa(self, tarefa):
        self.fila.adicionar(tarefa)

    def executarProximaTarefa(self):
        tarefa_executada = self.fila.remover()
        print(f"Executando tarefa: {tarefa_executada}")
        return tarefa_executada

    def executarTodasTarefas(self):
        tarefas_executadas = []
        while not self.fila.vazia():
            tarefas_executadas.append(self.executarProximaTarefa())
        return tarefas_executadas