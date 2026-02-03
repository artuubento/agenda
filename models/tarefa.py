from models.database import Database
from typing import Self, Any

class Tarefa:
        def __init__(self: Self, titulo_tarefa: str, data_conclusao: str = None, id: int = None) -> None:
                self.titulo_tarefa: str = titulo_tarefa
                self.data_conclusao: str = data_conclusao
                self.id: int = id
                # Atrbutos que pertencem ao OBJETO.

        def salvar_tarefa(self: Self) -> None:
                with Database('./data/tarefas.sqlite3') as db:
                        query: str = "INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
                        params: tuple = (self.titulo_tarefa, self.data_conclusao)
                        db.executar(query, params)
                        # POST;

        @staticmethod
        def obter_tarefas() -> list[Self]:
                with Database('./data/tarefas.sqlite3') as db:
                        query: str = "SELECT titulo_tarefa, data_conclusao FROM tarefas;"
                        resultados: list[Any] = db.buscar_tudo(query)
                        tarefas: list[Self] = [Tarefa(titulo, data) for titulo, data in resultados]
                        return tarefas
                        # GET;

        def excluir_tarefa(self) -> None:
                self.id