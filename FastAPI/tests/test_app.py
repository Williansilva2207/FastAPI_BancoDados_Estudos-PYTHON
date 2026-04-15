from http import HTTPStatus
from ORM.FastAPI.Fast_zero.UserSchema import UserPublicSchema
def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'name': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'name': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }
def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}

def test_read_users_with_users(client, user):
    user_schema = UserPublicSchema.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}

def test_update_user(client, user): 
    response = client.put(
        '/users/1',
        json={
            'name': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'name': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }

def test_update_integrity_error(client, user):
    # Criando um registro para "fausto"
    client.post( 
        '/users',
        json={
            'name': 'fausto',
            'email': 'fausto@example.com',
            'password': 'secret',
        },
    )

    # Alterando o user.username das fixture para fausto
    response_update = client.put( 
        f'/users/{user.id}',
        json={
            'name': 'fausto',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {
        'detail': 'Username or email already exists'
    }

def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}