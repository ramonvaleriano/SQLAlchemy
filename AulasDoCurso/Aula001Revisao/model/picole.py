import sqlalchemy
import sqlalchemy.orm as orm
from datetime import datetime
from model.sabor import Sabor
from typing import Optional, List
from model.model_base import ModelBase
from model.tipo_picole import TipoPicole
from model.ingrediente import Ingrediente
from model.conservante import Conservante
from model.tipo_embalagem import TipoEmbalagem
from model.aditivo_nutritivo import AditivoNutritivo


#  Um Picole pode ter vários ingredientes
ingredientes_picole = sqlalchemy.Table(
    'ingredientes_picole',
    ModelBase.metadata,
    sqlalchemy.Column('id_picole', sqlalchemy.Integer, sqlalchemy.ForeignKey('picoles.id')),
    sqlalchemy.Column('id_ingredientes', sqlalchemy.Integer, sqlalchemy.ForeignKey('ingredientes.id'))
)

#  Um Picole pode ter vários conservantes
conservantes_picole = sqlalchemy.Table(
    'conservantes_picole',
    ModelBase.metadata,
    sqlalchemy.Column('id_picole', sqlalchemy.Integer, sqlalchemy.ForeignKey('picoles.id')),
    sqlalchemy.Column('id_conservantes', sqlalchemy.Integer, sqlalchemy.ForeignKey('conservantes.id'))
)

#  Um picole pode ter vários aditivos nutritivos
aditivos_nutritivos_picole = sqlalchemy.Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    sqlalchemy.Column('id_picole', sqlalchemy.Integer, sqlalchemy.ForeignKey('picole.id')),
    sqlalchemy.Column('id_aditivos_nutritivos', sqlalchemy.Integer, sqlalchemy.ForeignKey('aditivos_nutritivos.id'))
)


class Picole(ModelBase):
    __tablename__ = 'picoles'

    id: int = sqlalchemy.Column(sqlalchemy.BigInteger, prymary_key=True, autoincrement=True)
    data_criacao: datetime = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now(), index=True)
    preco: float = sqlalchemy.Column(sqlalchemy.DECIMAL(8, 2), nullable=False)

    id_sabor: int = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Sabores.id'))
    sabor: Sabor = orm.relationship('Sabor', lazy='joined')

    id_tipo_embalagem: int = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: TipoEmbalagem = orm.relationship('TipoEmbalagem', lazy='joined')

    id_tipo_picole: int = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('tipos_picoles.id'))
    tipo_picole: TipoPicole = orm.relationship('TipoPicole', lazy='Joined')

    # Um picole pode ter vários ingredientes
    ingredientes: List[Ingrediente] = orm.relationship('Ingrediente', secondary=ingredientes_picole,
                                                       backref='ingredientes', lazy='joined')

    # Um picole pode ter vários conservantes ou nenhum
    conservantes: Optional[List[Conservante]] = orm.relationship('Conservante', secondary=conservantes_picole,
                                                                 backref='conservantes', lazy='joined')

    # Um picole pode ter vários aditivos nutritivos ou nenhum
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = orm.relationship('AditivoNutritivo',
                                                                             secondary=aditivos_nutritivos_picole,
                                                                             backref='aditivos_nutritivos',
                                                                             lazy='joined')

    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome}>, Sabor: {self.sabor.nome}, Preço: {self.preco}'