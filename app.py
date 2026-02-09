from flask import Flask, render_template, request, redirect, url_for
from models.tarefa import Tarefa

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html', titulo='Home')

@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    tarefas = None
    if request.method == 'POST':
        titulo_tarefa  = request.form["titulo-tarefa"]
        data_conclusao = request.form["data-conclusao"]
        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()

    tarefas = Tarefa.obter_tarefas()
    return render_template('agenda.html', titulo='Agenda', tarefas=tarefas)

@app.route('/delete/<int:idTarefa>') 
def delete(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.excluir_tarefa()
    return redirect(url_for('agenda'))

@app.route('/update/<int:idTarefa>', methods=['GET', 'POST'])
def update(idTarefa):
    if request.method == 'POST':
        novo_titulo = request.form["titulo-tarefa"]
        nova_data = request.form["data-conclusao"]
        tarefa = Tarefa(novo_titulo, nova_data, idTarefa)
        tarefa.atualizar_tarefa()
        return redirect(url_for('agenda'))
    tarefas = Tarefa.obter_tarefas()
    tarefa_selecionada = Tarefa.id(idTarefa)
    return render_template('agenda.html', tarefa_selecionada=tarefa_selecionada, tarefas=tarefas, titulo=f"Editando a tarefa ID: {idTarefa}")

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"