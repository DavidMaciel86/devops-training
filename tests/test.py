import pytest



def test_root():
    return {"message": "Hello World"}


def nova_rota():
    return {"test": True, "nume_aleatorio": random.randint(0, 57000)}


def create_estudante(estudante: Estudante):
    return  estudante


def update_estudante(id_estudante: int):
    return id_estudante > 0


def delete_estudante(estudante: int):
    return id_estudante > 0


class Estudante(BseModel):
    name: str
    curso: str
    ativo: bool
