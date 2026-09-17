from unittest.mock import patch

from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)

def test_root():
    response = client.get("/hello_world")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_new_rout():
    with patch('src.main.random.randint', return_value=12000):
        response = client.get("/funcao_test")

    assert response.status_code == 200
    assert response.json() == {"test": True, "nume_aleatorio": 12000}


def test_create_estudant():
    estudante_de_teste = {"nome": "João", "curso": "DevOps", "ativo": True}

    response = client.post("/estudantes/cadastro", json=estudante_de_teste)

    assert response.status_code == 200
    assert response.json() == estudante_de_teste


def test_negativo_update_estudant():
    # testa resultado negativo
    response = client.put("/estudantes/update/-1")

    assert response.status_code == 200
    assert response.json() is False


def test_positivo_update_estudant():
    # testa resultado positivo
    response = client.put("/estudantes/update/1")

    assert response.status_code == 200
    assert response.json() is True


def test_negativo_delete_estudant():
    # testa resultado negativo
    response = client.delete("/estudantes/delete/-2")

    assert response.status_code == 200
    assert response.json() is False


def test_positivo_delete_estudant():
    # testa resultado positivo
    response = client.delete("/estudantes/delete/2")

    assert response.status_code == 200
    assert response.json() is True
