from typing import List
from model.sabor import Sabor
from config.helpers import formata_data
from config.db_session import create_session
from model.aditivo_nutritivo import AditivoNutritivo


def select_todos_aditivos_nutritivos() -> None:

    with create_session() as session:
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo)
        print('*' * 100)
        print('Primeira foma de se obeter todos os dados dos aditivos Nutritivos')
        for an in aditivos_nutritivos:
            print(f'BD:{an}')
            print(f'ID: {an.id}')
            print(f'Nome: {an.nome}')
            print(f'Data Criacao: {formata_data(an.data_criacao)}')

    print('\n')

    with create_session() as session:
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all()
        print('*' * 100)
        print('Segunda foma de se obeter todos os dados dos aditivos Nutritivos')
        for an in aditivos_nutritivos:
            print(f'BD:{an}')
            print(f'ID: {an.id}')
            print(f'Nome: {an.nome}')
            print(f'Data Criacao: {formata_data(an.data_criacao)}')


def select_filtro_sabor(id_sabor: int):

    with create_session() as session:
        print('*' * 100)
        print('Primeira foma de se obeter todos os dados dos Sabores')
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).first()
        print(f'Qual o sabor encontrador pelo ID: {id_sabor}')
        print(f'ID: {sabor.id}')
        print(f'Nome: {sabor.nome}')
        print(f'Data Criacao: {formata_data(sabor.data_criacao)}')

    print('\n')

    with create_session() as session:
        print('*' * 100)
        print('Segunda foma de se obeter todos os dados dos Sabores')
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()
        print(f'Qual o sabor encontrador pelo ID: {id_sabor}')
        print(f'ID: {sabor.id}')
        print(f'Nome: {sabor.nome}')
        print(f'Data Criacao: {formata_data(sabor.data_criacao)}')

    print('\n')

    with create_session() as session:
        print('*' * 100)
        print('Terceira foma de se obeter todos os dados dos Sabores')
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one()
        print(f'Qual o sabor encontrador pelo ID: {id_sabor}')
        print(f'ID: {sabor.id}')
        print(f'Nome: {sabor.nome}')
        print(f'Data Criacao: {formata_data(sabor.data_criacao)}')

    with create_session() as session:
        print('*' * 100)
        print('Quarta foma de se obeter todos os dados dos Sabores')
        sabor: Sabor = session.query(Sabor).where(Sabor.id == id_sabor).one_or_none()
        print(f'Qual o sabor encontrador pelo ID: {id_sabor}')
        print(f'ID: {sabor.id}')
        print(f'Nome: {sabor.nome}')
        print(f'Data Criacao: {formata_data(sabor.data_criacao)}')


if __name__ == '__main__':
    #select_todos_aditivos_nutritivos()
    select_filtro_sabor(3)
