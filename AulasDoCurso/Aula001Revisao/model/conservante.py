import sqlalchemy
from datetime import datetime
from model.model_base import ModelBase


class Conservante(ModelBase):
    __tablename__ = 'conservantes'

    id: int = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now(), index=True)
    nome: str = sqlalchemy.Column(sqlalchemy.String(45), unique=True, nullable=False)
    descricao: str = sqlalchemy.Column(sqlalchemy.String(45), nullable=False)

    def __repr__(self):
        return f'<Conservante: {self.nome}>'
