from sqlite3 import Connection, Cursor, connect
from typing import Any

class Database:
    def __init__(self, db_name: str) -> None:
        self.connection: Connection = connect(db_name)
        self.cursor: Cursor = self.connection.cursor()

    def executar(self, query: str, params: tuple = ()) -> Cursor:
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor
    
    def buscar_todos(self, query: str, params: tuple = ()) -> list[Any]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def close(self) -> None:
        self.connection.close()


    # Métodos de entrada no contexto
    def __enter__(self):
        return self 
    

    # Métodos de saída do contexto
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


# hjyj