from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo


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


if __name__ == '__main__':
    insert_aditivo_nutritivo()
