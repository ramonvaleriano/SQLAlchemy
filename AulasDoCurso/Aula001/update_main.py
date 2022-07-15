"""
Para se realizar uma atulização, nós realizamos o 3 passos:
1 - Buscar o registro a ser atualizado
2 - Faz alteração no registro
3 - Salva o registro no banco de dados
"""

from models.sabor import Sabor
from models.picole import Picole
from conf.db_session import create_session


def atualiza_sabor(id_sabor: int, novo_nome: str) -> None:
    with create_session() as session:
        #  Passo 1: Buscar o dado desejado
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()
        if sabor:
            print(f'Sabor Anterior: {Sabor.nome}; Atualização: {novo_nome}')
            sabor.nome = novo_nome
            session.commit()
        else:
            print('Não existe o sabor selecionado: ')


if __name__ == '__main__':
    atualiza_sabor(1, 'Whey Protein')
