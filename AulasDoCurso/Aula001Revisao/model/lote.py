import sqlalchemy
import sqlalchemy.orm as orm
from datetime import datetime
from model.model_base import ModelBase
from model.tipo_picole import TipoPicole


class Lote(ModelBase):
    __tablename__ = 'lotes'

    id: int = sqlalchemy.Column(sqlalchemy.BigInteger, prymary_key=True, autoincrement=True)
    data_criacao: datetime = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now(), index=True)

    id_tipo_picole: int = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('tipos_picoles.id'))
    tipo_picole: TipoPicole = orm.relationship('TipoPicole', lazy='joined')

    quantidade: int = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    def __repr__(self) -> str:
        return f'<Lote: {self.id}>'
    