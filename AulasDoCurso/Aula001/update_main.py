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
    """
    Função para realizar a atualização do sabor
    :param id_sabor: ID do sabor a ser encontrado
    :param novo_nome: Novo nome para o sabor desejado
    :return: None
    """
    with create_session() as session:
        #  Passo 1: Buscar o dado desejado
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()
        if sabor:
            # Passo 2: Realizar a atulização desejada
            print(f'Sabor Anterior: {Sabor.nome}; Atualização: {novo_nome}')
            sabor.nome = novo_nome
            # Passo 3: Salvar o registro no banco de dados
            session.commit()
        else:
            print(f'Não existe o sabor selecionado com ID {id_sabor}')


def atualiza_picole(id_picole: int, novo_preco: float, novo_sabor: int = None) -> None:
    """
    Função responsável para atualizar o picole
    :param id_picole: ID do picole desejado
    :param novo_preco: Novo valor para o picole desejado
    :param novo_sabor: Novo sabor para o picole desejado
    :return: None
    """
    with create_session() as session:
        # Passo 1: Buscar o dado no banco de dados
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            # Passo 2: Realizar a atualização desejada
            picole.preco = novo_preco
            if novo_sabor:
                picole.id_sabor = novo_sabor
            # Passo 3: Salvar as alterações
            session.commit()

        else:
            print(f'Não exite dados com o ID: {id_picole}')


if __name__ == '__main__':
    # atualiza_sabor(1, 'Whey Protein')
    atualiza_picole(1, 3.34, 1)
