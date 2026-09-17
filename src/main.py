"""API FastAPI utilizada para treinamento de rotas e testes automatizados."""

# FastAPI é a classe principal do framework.
# app = FastAPI() cria a instância da aplicação.
# @app.get("/") registra uma rota HTTP do tipo GET no caminho raiz "/".
# A função assíncrona root() é executada quando uma requisição GET
# é feita para essa rota.
# O dicionário retornado pela função é convertido automaticamente
# pelo FastAPI em uma resposta no formato JSON.

import random
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Estudante(BaseModel):
    """Representa os dados de um estudante."""

    nome: str
    curso: str
    ativo: bool


@app.get("/hello_world")
async def root():
    return {"message": "Hello World"}


@app.get("/funcao_test")
async def new_rout():
    return {
        "test": True,
        "nume_aleatorio": random.randint(0, 57000)
    }


@app.post("/estudantes/cadastro")
async def create_estudant(estudante: Estudante):
    return estudante


@app.put("/estudantes/update/{id_estudante}")
async def update_estudant(id_estudante: int):
    return id_estudante > 0


@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudant(id_estudante: int):
    return id_estudante > 0
