from models.lote import Lote
from models.sabor import Sabor
from models.picole import Picole
from models.revendedor import Revendedor
from models.nota_fiscal import NotaFiscal
from conf.db_session import create_session
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.tipos_picole import TipoPicole
from models.tipo_embalagem import TipoEmbalagem
from models.aditivo_nutritivo import AditivoNutritivo


#  Adicionar Aditivo Nutritivo
def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print('Cadastro Aditivo Nutritivo')

    nome: str = str(input('Informe o nome do Aditivo Nutritivo: '))
    formula_quimica: str = str(input('Informe a Formula Quimica: '))

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)
        session.commit()

    return an


#  Adicionar Conservante
def insert_conservante() -> Conservante:
    print('Cadastro Conservante')

    nome: str = str(input('Nome do conservante: '))
    descricao: str = str(input('Descrição do conservante: '))

    co: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(co)
        session.commit()

    return co


#  Adicionar Ingrediente
def insert_ingrediente() -> Ingrediente:
    print('Cadatro de um ingrediente')

    nome: str = str(input('Nome do Ingrediente: '))
    ing: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ing)
        session.commit()

    return ing


#  Adicionar Revendedor
def insert_revendedor() -> Revendedor:
    print('Cadastro de um Revendedor')

    cnpj: str = str(input('Digite o cnpj do revendedor'))
    razao_social: str = str(input('Digite a razão social do revendedor: '))
    contato: str = str(input('Digite o contato desse revendedor: '))

    reven: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(reven)
        session.commit()

    return reven


#  Adicionar Sabor
def insert_sabor() -> None:
    print('Cadastro de um Sabor')

    nome: str = str(input('Qual o nome do sabor: '))

    sab: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sab)
        session.commit()

    print('Sabor adicionado com sucesso: ')
    print(f'Nome: {sab.nome}')


#  Adicionar tipo de embalagem
def insert_tipo_embalagem() -> None:
    print('Cadastro do tipo de embalagem: ')

    nome: str = str(input('Qual é o tipo de embalagem: '))

    tde: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(tde)
        session.commit()

    print('Tipo de embalagem cadastrada com sucesso: ')
    print(f'NOme: {tde.nome}')


#  Adicionar tipo de picole
def insert_tipo_picole() -> None:
    print('Cadastro de Tipo de Picole: ')

    nome: str = str(input('Adicionando tipo de picole: '))
    tdp: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tdp)
        session.commit()

    print('Cadastro de tipo de picole realizado com sucesso')
    print(f'Nome: {tdp.nome}')


#  Adicionando Lote
def insert_lote() -> Lote:
    print('Cadastrando Lote: ')

    id_tipo_picole: int = int(input('Informe o ID do tipo de picole: '))
    quantidade: int = int(input('Digite a quantidade de picoles: '))

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    with create_session() as session:
        session.add(lote)
        session.commit()

    return lote


#  Adicionar nota_fiscal
def insert_nota_fiscal() -> NotaFiscal:
    print('Cadastrar Nota Fiscal: ')

    valor: float = float(input('Entre com o valor: '))
    numero_serie: str = str(input('Entre com o número de série: '))
    description: str = str(input('Entrei coom a descrição da nota fiscal: '))

    id_revendedor: int = int(input('Entre com o ID do Revendendor: '))

    nota_fiscal: NotaFiscal = NotaFiscal(
        valor=valor,
        numero_serie=numero_serie,
        description=description,
        id_revendedor=id_revendedor
        )

    lote1 = insert_lote()
    nota_fiscal.lotes.append(lote1)

    with create_session() as session:
        session.add(nota_fiscal)
        session.commit()

    return nota_fiscal


#  Adicionar o Picolé
def insert_picole() -> Picole:
    print('Cadatro do picole: ')

    preco: float = float(input('Digite o valor do picole: '))
    id_sabor: int = int(input('Digite o ID do sabor: '))
    id_tipo_embalagem: int = int(input('Digite o id_tipo_de_embalagem: '))
    id_tipo_picole: int = int(input('Digite o tipo de picole: '))

    picole: Picole = Picole(preco=preco,
                            id_sabor=id_sabor,
                            id_tipo_embalagem=id_tipo_embalagem,
                            id_tipo_picole=id_tipo_picole
                            )

    ingrediente1 = insert_ingrediente()
    picole.ingredientes.append(ingrediente1)

    """conservantes = insert_conservante()
    picole.conservantes.append(conservantes)

    aditivos_nutritivos = insert_aditivo_nutritivo()
    picole.aditivos_nutritivos.append(aditivos_nutritivos)"""

    with create_session() as session:
        session.add(picole)
        session.commit()

    return picole


if __name__ == '__main__':
    """#  Adicionar Aditivo Nutritivo
    insert_aditivo_nutritivo()

    #  Adicionar Conservante
    insert_conservante()

    #  Adicionando Ingrediente
    insert_ingrediente()

    #  Adicionando Revendedor
    insert_revendedor()

    #  Adicionando Sabor
    insert_sabor()

    #  Adicionando Tipo de Embalagem
    insert_tipo_embalagem()

    #  Adicionando Tipo de Picole
    insert_tipo_picole()

    #  Adicionando Lote
    result_lote = insert_lote()

    #  Adicionando Nota Fiscal
    result_nota_fiscal = insert_nota_fiscal()"""

    #  Adicionando Picole
    result_picole = insert_picole()
    print(result_picole)
