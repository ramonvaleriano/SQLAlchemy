from typing import List
#  Funções de agregação
from sqlalchemy import func
from conf.helpers import formata_data
from conf.db_session import create_session
#  Select Simples
from models.sabor import Sabor
from models.revendedor import Revendedor
from models.aditivo_nutritivo import AditivoNutritivo
#  Select Compostos / Complexos
from models.picole import Picole


#  Select simples Get All -> SELECT * FROM aditivos_nutritivos;
def select_todos_aditivos_nutritivos() -> None:
    """
    Função criada para coletar todos os dados da tabela aditivos_nutritivos
    :return: None
    """
    with create_session() as session:
        #  Formaula 1 de se obter os dados:
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo)
        print('*'*100)
        print('Primeira foma de se obeter todos os dados dos aditivos Nutritivos')
        for an in aditivos_nutritivos:
            print(f'BD:{an}')
            print(f'ID: {an.id}')
            print(f'Nome: {an.nome}')
            print(f'Data Criacao: {formata_data(an.data_criacao)}')

        print('\n\n\n')

        #  Formula 2 de se obter os dados:
        print('*' * 100)
        print('Segunda foma de se obeter todos os dados dos aditivos Nutritivos')
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all()
        for an in aditivos_nutritivos:
            print(f'BD:{an}')
            print(f'ID: {an.id}')
            print(f'Nome: {an.nome}')
            print(f'Data Criacao: {formata_data(an.data_criacao)}')


#  Coletando dados via ID
def select_filtro_sabor(id_sabor: int) -> None:
    """
    Como capiturar um determinado dado por seu id
    :param id_sabor: ID do dados desejado
    :return: None
    """
    #  1° Forma de se realizar esse tipo de consulta
    print('*' * 100)
    print('Primeira foma de se obeter todos os dados dos Sabores')
    with create_session() as session:
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).first()
        print(f'Qual o sabor encontrador pelo ID: {id_sabor}')
        print(f'ID: {sabor.id}')
        print(f'Nome: {sabor.nome}')
        print(f'Data Criacao: {formata_data(sabor.data_criacao)}')

    print('\n')

    #  2° Forma de se realizar esse tipo de consulta
    print('*' * 100)
    print('Segunda foma de se obeter todos os dados dos Sabores')
    with create_session() as session:
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()
        print(f'Qual o sabor encontrador pelo ID: {id_sabor}')
        print(f'ID: {sabor.id}')
        print(f'Nome: {sabor.nome}')
        print(f'Data Criacao: {formata_data(sabor.data_criacao)}')

    print('*' * 100)
    print('Terceira foma de se obeter todos os dados dos Sabores, caso não encontre, devolve uma exeção')
    with create_session() as session:
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one()
        print(f'Qual o sabor encontrador pelo ID: {id_sabor}')
        print(f'ID: {sabor.id}')
        print(f'Nome: {sabor.nome}')
        print(f'Data Criacao: {formata_data(sabor.data_criacao)}')

    print('*' * 100)
    print('Quarta foma de se obeter todos os dados dos Sabores, caso não encontre, usando WHERE')
    with create_session() as session:
        sabor: Sabor = session.query(Sabor).where(Sabor.id == id_sabor).one_or_none()
        print(f'Qual o sabor encontrador pelo ID: {id_sabor}')
        print(f'ID: {sabor.id}')
        print(f'Nome: {sabor.nome}')
        print(f'Data Criacao: {formata_data(sabor.data_criacao)}')

    """
        Para todos os casos, usando o filter() ou where() nós podemos usar o first(), one_or_none() ou 
        o one()
    """


def select_complexo_picole() -> None:
    """
    Vamos criar uma query para todos os dados da tabela complexa, picole.
    :return: None
    """
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).all()
        for pic in picoles:
            print(pic)
            print(f'ID: {pic.id}')
            print(f'Data criação: {formata_data(pic.data_criacao)}')
            print(f'Sabor: {pic.sabor.nome}')
            print(f'Preço: {pic.preco}')


def select_order_by_sabor() -> None:
    """
    Criando um consulta de todos os dados na ordem que desejamos
    :return: None
    """

    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).order_by(Sabor.data_criacao.desc()).all()
        for sabor in sabores:
            print(f'{sabor}')
            print(f'{sabor.id}')
            print(f'{sabor.nome}')
            print(f'{sabor.data_criacao}')


def select_group_by_picole() -> None:
    """
    Função responsável por coletar todos os dados de forma agrupada
    :return: None
    """
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).group_by(Picole.id, Picole.id_tipo_picole).all()

        for picole in picoles:
            print(f'{picole}')
            print(f'{picole.id}')
            print(f'{picole.id_tipo_picole}')
            print(f'{picole.tipo_picole.nome}')
            print(f'{picole.sabor.nome}')


def select_limit_sabore() -> None:
    """
    Consultando todos os dados com limite de dados retornados
    :return: None
    """
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).limit(10)
        for sabor in sabores:
            print(sabor)
            print(sabor.id)
            print(sabor.nome)


def select_count_revendedores() -> None:
    """
    Função responsável por contar a quantidade de revendedores
    :return: None
    """
    with create_session() as session:
        revendores: int = session.query(Revendedor).count()

        print(f'A quantidade de revendedores é: {revendores}')


def select_agreggate_picole() -> None:
    """
    Função responsável por incrementar as funções de agregação na query
    :return: None
    """
    with create_session() as sesssion:
        picoles: List = sesssion.query(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('mais_barato'),
            func.max(Picole.preco).label('mais_caro'),
        ).all()
        print(picoles)
        print(f'A soma de todos os picoles é: {picoles[0][0]}')
        print(f'A media de todos os picoles é: {picoles[0][1]}')
        print(f'A mais barato de todos os picoles é: {picoles[0][2]}')
        print(f'A mais caro de todos os picoles é: {picoles[0][3]}')


if __name__ == '__main__':
    # SELECT todos dados da tabela aditivos_nutritivos
    #select_todos_aditivos_nutritivos()

    # SELECT determinando pelo ID do Sabor
    #select_filtro_sabor(3)

    # SELECT todos dados da tabela complexa Picole
    #select_complexo_picole()

    # SELECT todos os dados ordenados pela data de criação
    #select_order_by_sabor()

    # SELECT todos os dados do picole de forma agrupada
    #select_group_by_picole()

    # SELECT todos os dados, com limitação de dados que serão retornados
    #select_limit_sabore()

    # SELECT a quantidade de revendedores que nós temos
    #select_count_revendedores()

    # SELECT das funções de agregação dos picoles
    select_agreggate_picole()
