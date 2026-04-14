from dataclasses import asdict
from sqlalchemy import select
from FastBd.models import User
from ORM.Test.conftest import mock_db_time


def test_create_user(session):
    with mock_db_time(model=User) as time:
        new_user = User(username='alice', password='secret', email='teste@test')
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user)== { 
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,  
    }
#O método .scalar é usado para performar buscas no banco (queries). Ele pega o primeiro resultado da busca 
# e faz uma operação de converter o resultado do banco de dados 
# em um Objeto criado pelo SQLAlchemy, nesse caso, caso encontre um resultado, ele irá converter na classe User