from model.lote import Lote
from model.sabor import Sabor
from model.picole import Picole
from model.revendedor import Revendedor
from model.tipo_picole import TipoPicole
from model.conservante import Conservante
from model.ingrediente import Ingrediente
from model.notal_fiscal import NotaFiscal
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


def insert_lote() -> Lote:

    id_tipo_picole: int = int(input('Digite id do tipo de picole: '))
    quantidade: int = int(input('Digite a quantidade de picoles: '))

    lot: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    with create_session() as session:
        session.add(lot)
        session.commit()

    return lot


def insert_nota_fiscal() -> NotaFiscal:
    valor: float = float(input('Digite o valor da nota fiscal: '))
    numero_serie: str = str(input('Digite agora o número de série da nota fiscal: '))
    descricao: str = str(input('Digite a descrição da Nota fiscal: '))
    id_revendedor: int = int(input('Digite o ID do revendedor: '))

    ntf: NotaFiscal = NotaFiscal(
        valor=valor,
        numero_serie=numero_serie,
        descricao=descricao,
        id_revendedor=id_revendedor
    )

    lotes_ = insert_lote()
    ntf.lotes.append(lotes_)

    with create_session() as session:
        session.add(ntf)
        session.commit()

    return ntf


def insert_picole() -> Picole:
    preco: float = float(input('Digite o preço do picole: '))
    id_sabor: int = int(input('Digite o ID do sabor: '))
    id_tipo_embalagem: int = int(input('Digite o ID do tipo de embalagem: '))
    id_tipo_picole: int = int(input('Digite o ID do tipo de picole: '))

    ingredientes = insert_ingrediente()
    conservantes = insert_conservante()
    aditivos_nutritivos = insert_aditivo_nutritivo()

    pic: Picole = Picole(
        preco=preco,
        id_sabor=id_sabor,
        id_tipo_embalagem=id_tipo_embalagem,
        id_tipo_picole=id_tipo_picole,
    )
    pic.ingredientes.append(ingredientes)
    pic.conservantes.append(conservantes)
    pic.aditivos_nutritivos.append(aditivos_nutritivos)

    with create_session() as session:
        session.add(pic)
        session.commit()

    return pic


if __name__ == '__main__':
    """
    result_aditivo_nutritivo = insert_aditivo_nutritivo()
    result_conservante = insert_conservante()
    result_ingrediente = insert_ingrediente()
    result_revendedor = insert_revendedor()
    result_sabor = insert_sabor()
    result_tipo_embalagem = insert_tipo_embalagem()
    result_tipo_picole = insert_tipo_de_picole()
    result_lote = insert_lote()
    result_nota_fiscal = insert_nota_fiscal()
    """
    result_picole = insert_picole()
    print(result_picole)

