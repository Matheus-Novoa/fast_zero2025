from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero2025.app import app


def test_root_deve_retornar_ola_mundo():
    """'
    Esse teste tem 3 etapas:
    - A: Arrange - Arranjo
    - A: Act = Executa a coisa (o SUT)
    - A: Assert - Garanta que A é A
    """
    # A: Arrange
    client = TestClient(app)
    # A: Act
    response = client.get('/')
    # A: Assert
    assert response.json() == {'message': 'Olá Mundo!'}
    assert response.status_code == HTTPStatus.OK
