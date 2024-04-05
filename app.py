from flask import Flask, jsonify
from robo_de_limpeza import RoboDeLimpeza

app = Flask(__name__)
robo = RoboDeLimpeza()

@app.route('/executarTodasTarefas', methods=['GET'])
def executar_todas_tarefas():
    tarefas_executadas = robo.executarTodasTarefas()
    if len(tarefas_executadas) == 0:
        return jsonify({"mensagem": "Não há tarefas pendentes a serem executadas",
                        "tarefasExecutadas": tarefas_executadas}), 204
    else:
        return jsonify({"mensagem": "Todas as tarefas foram executadas com sucesso.",
                        "tarefasExecutadas": tarefas_executadas}), 200

if __name__ == '__main__':
    app.run(debug=True)