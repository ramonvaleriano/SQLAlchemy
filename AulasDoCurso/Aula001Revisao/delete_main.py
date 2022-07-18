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


if __name__ == '__main__':
    delete_picole(2)
