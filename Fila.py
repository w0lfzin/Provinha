class Fila:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def remover(self):
        if self.tarefas:
            return self.tarefas.pop(0)
        else:
            raise Exception("A fila de tarefas está vazia.")

    def vazia(self):
        return len(self.tarefas) == 0