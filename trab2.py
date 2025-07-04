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


def classificacao(jogo: Jogo, criterio: CriterioDesempate) -> int:
    '''
    A função vai receber um jogo *jogo: Jogo* e criterio *criterio: CriterioDesempate*,
    vai calcular a tabela dos times em relação aos jogos e vai retornar um inteiro.
    Exemplos:
    '''