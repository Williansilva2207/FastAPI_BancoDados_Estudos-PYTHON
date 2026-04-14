from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user(client):
    response = client.post(  # corrigido (era "reponse")
        "/users/",
        json={
            "name": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "name": "alice",
        "email": "alice@example.com",
        "id": 1,
    }


def test_read_users(client):
    # cria usuário antes
    client.post(
        "/users/",
        json={
            "name": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    response = client.get("/users/")  # corrigido (removido '?')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "name": "alice",
                "email": "alice@example.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    # cria usuário antes
    client.post(
        "/users/",
        json={
            "name": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    response = client.put(
        "/users/1",
        json={
            "name": "bob",
            "email": "bob@example.com",
            "password": "mynewpassword",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "name": "bob",
        "email": "bob@example.com",
        "id": 1,
    }


def test_delete_user(client):
    # cria usuário antes
    client.post(
        "/users/",
        json={
            "name": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted"}

def test_create_user_test(client):
    # cria usuário antes
    response = client.post(
        "/users/test",
        json={
            "name": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "name": "alice",
        "email": "alice@example.com",
        "id": 1,
    }