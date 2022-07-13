from models.sabor import Sabor
from models.revendedor import Revendedor
from conf.db_session import create_session
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.tipos_picole import TipoPicole
from models.tipo_embalagem import TipoEmbalagem
from models.aditivo_nutritivo import AditivoNutritivo


#  Adicionar Aditivo Nutritivo
def insert_aditivo_nutritivo() -> None:
    print('Cadastro Aditivo Nutritivo')

    nome: str = str(input('Informe o nome do Aditivo Nutritivo: '))
    formula_quimica: str = str(input('Informe a Formula Quimica: '))

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)
        session.commit()

    print('Aditivo Nutritivo cadastrado com sucesso.')
    print(f'Id: {an.id}')
    print(f'Nome: {an.nome}')


#  Adicionar Conservante
def insert_conservante() -> None:
    print('Cadastro Conservante')

    nome: str = str(input('Nome do conservante: '))
    descricao: str = str(input('Descrição do conservante: '))

    co: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(co)
        session.commit()

    print('Conservante adicionado com sucesso.')
    print(f'Id: {co.id}')
    print(f'Nome: {co.nome}')
    print(f'Descricao: {co.descricao}')


#  Adicionar Ingrediente
def insert_ingrediente() -> None:
    print('Cadatro de um ingrediente')

    nome: str = str(input('Nome do Ingrediente: '))
    ing: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ing)
        session.commit()

    print('Ingrediente adicionado: ')
    print(f'ID: {ing.id}')
    print(f'Nome: {ing.nome}')


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


if __name__ == '__main__':
    #  Adicionar Aditivo Nutritivo
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
