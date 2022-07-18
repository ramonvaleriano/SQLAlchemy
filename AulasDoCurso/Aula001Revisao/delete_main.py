from typing import Optional
from model.picole import Picole
from model.revendedor import Revendedor
from config.db_session import create_session


def delete_picole(id_picole: int) -> None:
    with create_session() as session:
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        if picole:
            session.delete(picole)
            session.commit()
        else:
            print('Não existe o picole desejado!')


def delete_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()
        if revendedor:
            session.delete(revendedor)
            session.commit()
        else:
            print('Não existe o revendedor desejado!')


if __name__ == '__main__':
    #delete_picole(2)
    #delete_revendedor(22)
    print('Deletando dados')
