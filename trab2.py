from enum import Enum, auto
from dataclasses import dataclass

class CriterioDesempate(Enum):
    '''
    Essa classe vai desempenhar em relação ao critério de desempate dos jogos do Brasileirão.
    '''
    PONTO = auto()
    VITORIA = auto()
    SALDO_GOL = auto()
    LETRA = auto()


@dataclass
class Jogo:
    '''
    Essa classe vai desempenhar em relação ao jogo do Brasileirão, tendo como atributos: anfitrião(Mandante),
    gols do anfitrião, visitante e gols do visitante.
    '''
    anfitriao: str
    anf_gol: int
    visitante: str
    vis_gol: int


def classificacao(jogo: list[Jogo], criterio: CriterioDesempate) -> int:
    '''
    A função vai receber um jogo *jogo: Jogo* e criterio *criterio: CriterioDesempate*,
    vai calcular a tabela dos times em relação aos jogos e vai retornar um inteiro.
    Exemplos:
    '''
    i: int = 0
    anfiGol = jogo[i].anf_gol
    visGol = jogo[i].vis_gol
    cont_anf = 0 
    cont_vis = 0
    while i < len(jogo):
        if criterio == CriterioDesempate.PONTO:
            if anfiGol > visGol:
                cont_anf += 3
            elif visGol > anfiGol:
                cont_vis += 3
            else:
                cont_anf += 1
                cont_vis += 1