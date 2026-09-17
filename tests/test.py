from unittest.mock import patch
from src.main import *


def test_root():
    assert root() == {"message": "Hello World"}


def test_new_rout():
    with patch('random.randint', return_value=12000):
        result = new_rout()

    assert result == {"test": True, "nume_aleatorio": 12000}


def test_create_estudant(estudante: Estudante):
    estudante_de_teste = Estudante(nome="João", curso="DevOps", ativo=True)
    assert estudante_de_teste == create_estudant()


def test_negativo_update_estudant(id_estudante: int):
    # testa resultado negativo
    assert not update_estudant(-1)


def test_positivo_update_estudant(id_estudante: int):
    # testa resultado positivo
    assert update_estudant(1)


def test_negativo_delete_estudant(id_estudante: int):
    assert not delete_estudant(-2)


def test_positivo_delete_estudant(id_estudante: int):
    assert delete_estudant(2)


class Estudante(BaseModel):
    nome: str
    curso: str
    ativo: bool
