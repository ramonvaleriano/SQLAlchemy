"""
Para se deletar um registro é necessário realizar alguns passos:
1 - Buscar o registro a ser deletado
2 - Deletar o registro
3 - Salvar a auteração
"""

from typing import Optional
from models.picole import Picole
from models.revendedor import Revendedor
from conf.db_session import create_session


def deletar_picole(id_picole: int) -> None:
    """
    Função responsável por deletar um registro da tabela picole
    :param id_picole: ID do picole desejado
    :return: None
    """
    with create_session() as session:
        #  1° Passo: Encontrar o registro a ser deletado
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            #  2° Passo: Deletar o registro
            session.delete(picole)
            #  3° Passo: Salvar auterações
            session.commit()

        else:
            print('Não há regristro com esse picolé')


def deletar_revendedor(id_revendedor: int) -> None:
    """
    Função responsavel por deleter um revendedor
    :param id_revendedor: ID do revendedor
    :return: None
    """
    with create_session() as session:
        #  1° Passo: Encontra o registro pelo ID
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            print(f'O ID do revendedor: {revendedor.id}')
            print(f'A razão social o revendedor: {revendedor.razao_social}')
            #  2° Passo: Deletar o registro
            session.delete(revendedor)
            #  3° Passo: Salvar a auteração
            session.commit()


        else:
            print('Não há registro com para esse revendedor.')
            print(f'O ID desejado era: {id_revendedor}')


if __name__ == '__main__':
    #  Deletar um Picole
    #deletar_picole(5)

    #  Deletar um revendedor
    deletar_revendedor(61)
