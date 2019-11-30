from fastapi import FastAPI

TAREFAS = [{"id":1, "titulo": "comprar ovos"},
            {"id":2, "titulo": "comprar sabonete"}]
            
app = FastAPI()

@app.get('/tarefas')
def listar():
    return TAREFAS
