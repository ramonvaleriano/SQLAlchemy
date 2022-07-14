from model.sabor import Sabor
from model.revendedor import Revendedor
from model.tipo_picole import TipoPicole
from model.conservante import Conservante
from model.ingrediente import Ingrediente
from config.db_session import create_session
from model.tipo_embalagem import TipoEmbalagem
from model.aditivo_nutritivo import AditivoNutritivo


def insert_aditivo_nutritivo() -> AditivoNutritivo:
    nome: str = str(input('Digite o nome do aditivo Nutritivo: '))
    formula_quimica: str = str(input('Digite a formula quimica do aditivo nutritivo: '))

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)
        session.commit()

    return an


def insert_conservante() -> Conservante:
    nome: str = str(input('Digite o nome do conservante: '))
    descricao: str = str(input('Digite a descrição do conservante: '))

    con: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(con)
        session.commit()

    return con


def insert_ingrediente() -> Ingrediente:
    nome: str = str(input('Digite o nome do ingrediente: '))

    ing: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ing)
        session.commit()

    return ing


def insert_revendedor() -> Revendedor:
    cnpj: str = str(input('Digite o CNPJ do revendedor: '))
    razao_social: str = str(input('Digite a Razão social do revendedor: '))
    contato: str = str(input('Digite o contato do revendedor: '))

    rev: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(rev)
        session.commit()

    return rev


def insert_sabor() -> Sabor:
    nome: str = str(input('O nome do sabor: '))

    sab: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sab)
        session.commit()

    return sab


def insert_tipo_embalagem() -> TipoEmbalagem:
    nome: str = str(input('Nome do tipo de embalagem: '))

    tem: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(tem)
        session.commit()

    return tem


def insert_tipo_de_picole() -> TipoPicole:
    nome: str = str(input('Digite o nome do tipo de picole: '))

    tp: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tp)
        session.commit()

    return tp


if __name__ == '__main__':
    """
    result_aditivo_nutritivo = insert_aditivo_nutritivo()
    result_conservante = insert_conservante()
    result_ingrediente = insert_ingrediente()
    result_revendedor = insert_revendedor()
    result_sabor = insert_sabor()
    result_tipo_embalagem = insert_tipo_embalagem()
    result_tipo_picole = insert_tipo_de_picole()
    """

