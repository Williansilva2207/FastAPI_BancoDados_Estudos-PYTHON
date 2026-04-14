import pytest
from FastAPIFromZero.FastAPIZero.app import app, database
from fastapi.testclient import TestClient
from sqlalchemy import create_engine 
from sqlalchemy.orm import Session
from ORM.FastBd.models import table_registry


@pytest.fixture
def client():
    database.clear()  # limpa antes de cada teste
    return TestClient(app)

@pytest.fixture
def session():
    #cria um mecanismo de banco de dados SQLite em memória usando SQLAlchemy. 
    #Este mecanismo será usado para criar uma sessão de banco de dados para nossos testes.
    engine = create_engine('sqlite:///:memory:') 
    #cria todas as tabelas no banco de dados de teste antes de cada teste que usa a fixture session.
    table_registry.metadata.create_all(engine)
    #cria uma sessão Session para que os testes possam se comunicar com o banco de dadosvia engine.
    with Session(engine) as session:
        #fornece uma instância de Session que será injetada em cada teste que solicita a fixture session. 
        #Essa sessão será usada para interagir com o banco de dados de teste.
        yield session
    #após cada teste que usa a fixture session, todas as tabelas do banco de dados de teste são eliminadas, 
    #garantindo que cada teste seja executado contra um banco de dados limpo.
    table_registry.metadata.drop_all(engine)

