from typing import List
#  Funções de agregação
from sqlalchemy import func
from conf.helpers import formata_data
from conf.db_session import create_session
#  Select Simples
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor
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

if __name__ == '__main__':
    # SELECT todos dados da tabela aditivos_nutritivos
    #select_todos_aditivos_nutritivos()

    # SELECT determinando pelo ID do Sabor
    select_filtro_sabor(3)
