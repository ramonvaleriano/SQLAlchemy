import sqlalchemy
from pathlib import Path
from typing import Optional
from model.model_base import BaseModel
from sqlalchemy.future.engine import Engine
from sqlalchemy.orm import Session, sessionmaker


__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    global __engine

    if sqlite:
        arquivo_db = 'db/picole.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)
        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sqlalchemy.create_engine(url=conn_str, echo=False, connect_args={'check_same_thread': False})

    else:

        conn_str = 'postgresql://postgres:*******@localhost:5432/picoles'
        __engine = sqlalchemy.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()

    return session


def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()

    BaseModel.metadata.drop_all(__engine)
    BaseModel.metadata.create_all(__engine)

