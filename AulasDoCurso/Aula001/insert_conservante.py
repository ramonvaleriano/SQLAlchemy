from conf.db_session import create_session
from models.conservante import Conservante


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

if __name__ == '__main__':
    insert_conservante()