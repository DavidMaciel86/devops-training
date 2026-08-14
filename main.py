# FastAPI é a classe principal do framework.
# app = FastAPI() cria a instância da aplicação.
# @app.get("/") registra uma rota HTTP do tipo GET no caminho raiz "/".
# A função assíncrona root() é executada quando uma requisição GET
# é feita para essa rota.
# O dicionário retornado pela função é convertido automaticamente
# pelo FastAPI em uma resposta no formato JSON.

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/nova_rota")
async def nova_rota() -> dict:
    return {"rota": "teste nova rota: OK!"}
