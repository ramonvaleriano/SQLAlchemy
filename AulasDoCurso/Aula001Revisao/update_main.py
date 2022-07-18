from typing import Optional
from model.sabor import Sabor
from model.picole import Picole
from config.db_session import create_session
from model.aditivo_nutritivo import AditivoNutritivo


def update_aditivo_nutritivo(id_aditivo_nutritivo: int, novo_sabor: str, formula_quimica: str) -> None:
    with create_session() as session:
        aditivo_nutritivo: Optional[AditivoNutritivo] = session.query(AditivoNutritivo).filter(AditivoNutritivo.id == id_aditivo_nutritivo).one_or_none()
        if aditivo_nutritivo:
            aditivo_nutritivo.nome = novo_sabor
            aditivo_nutritivo.formula_quimica = formula_quimica
            session.commit()
        else:
            print('Aditivo Nutritivo não encontrado!')


def uptade_sabor(id_sabor: int, novo_sabor: str) -> None:
    with create_session() as session:
        sabor: Optional[Sabor] = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()
        if sabor:
            sabor.nome = novo_sabor
            session.commit()
        else:
            print('Não existe esse sabor!')


def update_picole(id_picole: int, id_novo_sabor: int, novo_preco: float) -> None:
    with create_session() as session:
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        if picole:
            picole.preco = novo_preco
            picole.id_sabor = id_novo_sabor
            session.commit()
        else:
            print('Não exite o picole desejado!')


if __name__ == '__main__':
    #update_aditivo_nutritivo(1, 'Whey Protein', 'Proteina Soro do Leite')
    #uptade_sabor(1, 'Whey Protein Chocolate')
    update_picole(1, 1, 10.43)
