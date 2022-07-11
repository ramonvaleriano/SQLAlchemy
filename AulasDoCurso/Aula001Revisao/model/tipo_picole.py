import sqlalchemy
from datetime import datetime
from model.model_base import ModelBase


class TipoPicole(ModelBase):
    __tablename__ = 'tipos_picoles'

    id: int = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now(), index=True)
    nome: str = sqlalchemy.Column(sqlalchemy.String(45), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<Tipo de Picole: {self.nome}>'
