import sqlalchemy
from typing import List
from model.lote import Lote
import sqlalchemy.orm as orm
from datetime import datetime
from model.model_base import ModelBase
from model.revendedor import Revendedor


# Um nota fiscal pode ter vários lotes
lotes_nota_fiscal = sqlalchemy.Table(
    'lotes_notal_fiscal',
    ModelBase.metadata,
    sqlalchemy.Column('id_notal_fiscal', sqlalchemy.Integer, sqlalchemy.ForeignKey('notas_fiscais.id')),
    sqlalchemy.Column('id_lote', sqlalchemy.Integer, sqlalchemy.ForeignKey('lotes.id'))
)


class NotaFiscal(ModelBase):
    __tablename__ = 'notas_fiscais'

    id: int = sqlalchemy.Column(sqlalchemy.BigInteger, unique=True, autoincrement=True)
    data_criacao: datetime = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now(), index=True)
    valor: float = sqlalchemy.Column(sqlalchemy.DECIMAL(8, 2), nullable=False)
    numero_serie: str = sqlalchemy.Column(sqlalchemy.String(45), unique=True, nullable=False)
    description: str = sqlalchemy.Column(sqlalchemy.String(200), nullable=False)

    id_revendedor: int = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('revendedores.id'))
    revendedor: Revendedor = orm.relationship('Revendedor', lazy='joined')

    #  Uma nota fiscal pode conter vários lotes, e um lote está ligado a uma nota fiscal
    lotes: List[Lote] = orm.relationship('Lote', secondary=lotes_nota_fiscal, backref='lote', lazy='dynamic')

    def __repr__(self) -> str:
        return f'<Nota Fiscal: {self.numero_serie}>'
