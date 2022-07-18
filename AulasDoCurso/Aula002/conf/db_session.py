"""
    Vamos criar um projeto que possa usar tanto o SQLite, tanto quanto o PostgreSQL
"""

import sqlalchemy
from pathlib import Path
import models.__all_models
from typing import Optional
from models.model_base import ModelBase
from sqlalchemy.future.engine import Engine
from sqlalchemy.orm import sessionmaker, Session


"""
    :ModelBase: A usáremos para manipular nosso banco de dados, criar nossas tabelas, deletar
    as tabelas em nosso banco de dados, caso nós venhamos a precisar. Porém quando nós criarmos
    nossa model, ele será nossa base para criação dos dados.
    :sessiomaker: Como o nome mesmo já diz, é o criador de sessão.
    :Path: Vamos usar ele para criar diretorio, ou arquivo. Nesse caso, com o foco no SQLite.
    :Optional: Usando para tipar como opcional um determinado tipo de dado.
    :Session: Vamos criar objeto com base nesse tipo.
    :Engine: Vamos criar uma função para criar um Engine.
"""

__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    """
    Função responsável pela configuração da conexão do bando de dados.
    :param sqlite: Usaremos o sqlite como opção para caso nós venhamos desejar usar o sqlite
    :return: Caso sejá realizado com sucesso um Engine, caso não None
    """
    global __engine

    if __engine:
        return __engine

    if sqlite:
        # Caso seja usado o SQLite
        arquivo_db = 'db/picole.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)
        conn_str = f'sqlite:///{arquivo_db}'  # String de conexão
        __engine = sqlalchemy.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False})

    else:
        # Caso venhamos a usar o PostgreSQL
        conn_str = 'postgresql://postgres:*********@localhost:5432/picoles'
        __engine = sqlalchemy.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    """
    Função responsável por criar um sessão, ou seja uma conexão em si.
    :return: Caso positivo cria uma Session, cria a conexão.
    """
    global __engine

    if not __engine:
        create_engine()  # Caso você venha a usar o sqlite usar o create_engine(True)

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()

    return session


def create_tables() -> None:
    """
    Função responsável por criar as tabelas
    :return: None
    """
    global __engine

    if not __engine:
        create_engine()  # Caso você venha a usar o sqlite usar o create_engine(True)

    ModelBase.metadata.drop_all(__engine)    # Deletar todas as tabelas
    ModelBase.metadata.create_all(__engine)  # Criar todas as tabelas desejadas novamente
