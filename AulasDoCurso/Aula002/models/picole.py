import sqlalchemy
import sqlalchemy.orm as orm
from datetime import datetime
from models.sabor import Sabor
from typing import List, Optional
from models.model_base import ModelBase
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.tipos_picole import TipoPicole
from models.tipo_embalagem import TipoEmbalagem
from models.aditivo_nutritivo import AditivoNutritivo

# Picole pode ter varios ingredientes:
ingredientes_picole = sqlalchemy.Table(
    'ingredientes_picole',
    ModelBase.metadata,
    sqlalchemy.Column('id_picole', sqlalchemy.ForeignKey('picoles.id')),
    sqlalchemy.Column('id_ingrediente', sqlalchemy.ForeignKey('ingredientes.id'))
)

# Picole pode ter vários conservantes
conservantes_picole = sqlalchemy.Table(
    'conservantes_picole',
    ModelBase.metadata,
    sqlalchemy.Column('id_picole', sqlalchemy.ForeignKey('picoles.id')),
    sqlalchemy.Column('id_conservante', sqlalchemy.ForeignKey('conservante.id'))
)

# Picole pode ter vários aditivos nutritivos
aditivos_nutritivos_picole = sqlalchemy.Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    sqlalchemy.Column('id_picole', sqlalchemy.ForeignKey('picoles.id')),
    sqlalchemy.Column('id_aditivo_nutritivo', sqlalchemy.ForeignKey('aditivos_nutritivos.id'))
)


class Picole(ModelBase):
    __tablename__ = 'picoles'

    id: int = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now(), index=True)
    preco: float = sqlalchemy.Column(sqlalchemy.DECIMAL(8, 2), unique=False, nullable=False)

    id_sabor: int = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('sabores.id'))  # Tabela.Campo
    sabor: Sabor = orm.relationship('Sabor', lazy='joined')  # Montando o relacionamento para o SQLAlchemy

    id_tipo_embalagem: int = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: TipoEmbalagem = orm.relationship('TipoEmbalagem', lazy='joined')

    id_tipo_picole: int = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('tipos_picole.id'))
    tipo_picole: TipoPicole = orm.relationship('TipoPicole', lazy='joined')

    # Um picole pode ter varios ingredientes
    ingredientes: List[Ingrediente] = orm.relationship('Ingrediente', secondary=ingredientes_picole,
                                                       backref='ingrediente', lazy='joined')

    # Um picole pode ter vários conservantes ou nenhum
    conservantes: Optional[List[Conservante]] = orm.relationship('Conservante', secondary=conservantes_picole,
                                                                 backref='conservante', lazy='joined')

    # Um picole pode ter vários aditivos nutritivos ou nenhum
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = orm.relationship('AditivoNutritivo',
                                                                             secondary=aditivos_nutritivos_picole,
                                                                             backref='aditivo_nutritivo', lazy='joined')

    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome}>, Sabor: {self.sabor.nome}, Preço: {self.preco}'
