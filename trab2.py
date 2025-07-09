from enum import Enum, auto
from dataclasses import dataclass

class CriterioDesempate(Enum):
    '''
    Essa classe vai desempenhar em relação ao critério de desempate dos jogos do Brasileirão,
    sendo por pontos, vitorias, saldo de gols e letra em ordem alfabética.
    '''
    PONTO = auto()
    VITORIA = auto()
    SALDO_GOL = auto()
    LETRA = auto()


@dataclass
class Time:
    '''
    Essa classe vai desempenhar em relação ao times do Brasileirão, sendo eles:
    nome, pontos, vitoria, empate, derrota, gol_marcado, gol_contra.
    '''
    nome: str
    pontos: int
    vitoria: int
    empate: int
    derrota: int
    gol_marcado: int
    gol_contra: int
    jogos_anf: int
    jogos_vis: int


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

def encontra_nome_time(nome: str, lst_times: list[Time]) -> list[Time]:
    '''
    A função vai receber um nome *nome: str* e uma lista de times *lst_times: list[Time]*,
    vai verificar se tem um time na lista, caso contrário vai adicionar esse time na lista
    e retornar a lista com os times.
    Exemplos:
    >>> lst_times: list[Time] = [Time('Flamengo', 'Grêmio', 'Palmeiras'])
    >>> encontra_nome_time('Flamengo', lst_times)
    [Time('Flamengo', 'Grêmio', 'Palmeiras')]
    >>> encontra_nome_time('Internacional', lst_times)
    [Time('Flamengo', 'Grêmio', 'Palmeiras', 'Internacional')]
    >>> encontra_nome_time('Grêmio', lst_times)
    [Time('Flamengo', 'Grêmio', 'Palmeiras', 'Internacional')]
    '''
    time_enc: Time
    for i in lst_times:
        if lst_times[i].nome == nome:
            time_enc = lst_times[i]
    time_novo = lst_times.append(time_enc)
    return time_novo


def criterios(lst_times: list[Time], lst_jogos: list[Jogo], criterio: CriterioDesempate) -> list[Time]:
    '''
    A função vai receber um jogo *jogo: Jogo* e criterio *criterio: CriterioDesempate*,
    vai calcular a tabela dos times em relação aos jogos 
    Exemplos:
    
    '''
    i: int = 0
    anfiGol = criterio.anf_gol
    visGol = criterio.vis_gol
    cont_anf = 0 
    cont_vis = 0
    while i < len(lst_times):
        if criterio == CriterioDesempate.PONTO:
            if anfiGol > visGol:
                cont_anf += 3
            elif visGol > anfiGol:
                cont_vis += 3
            else:
                cont_anf += 1
                cont_vis += 1


def saldo_gol():
    '''
    A função vai calcular o saldo de gols.
    '''


