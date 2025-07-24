from enum import Enum, auto
from dataclasses import dataclass
import sys


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
    nome, pontos, vitoria, gol_marcado, gol_contra, saldo_gol, anf_jogos, anf_pontos.
    '''
    nome: str
    pontos: int
    vitoria: int
    gol_marcado: int
    gol_contra: int
    saldo_gol: int
    anf_jogos: int
    anf_pontos: int


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


def encontra_nome_time(nome: str, lst_times: list[Time]) -> None:
    '''
    A função vai receber um nome *nome: str* e uma lista de times *lst_times: list[Time]*,
    vai verificar se tem um time na lista, caso contrário vai adicionar esse time na lista
    e retornar a lista com os times.
    Exemplos:
    >>> flamengo: Time = Time('Flamengo', 0, 0, 0, 0, 0, 0, 0)
    >>> gremio: Time = Time('Grêmio', 0, 0, 0, 0, 0, 0, 0)
    >>> sao_paulo: Time = Time('São Paulo', 0, 0, 0, 0, 0, 0, 0)
    >>> corinthians: Time = Time('Corinthians', 0, 0, 0, 0, 0, 0, 0)
    >>> lst_times: list[Time] = [flamengo, gremio, sao_paulo, corinthians]
    >>> encontra_nome_time('Palmeiras', lst_times)
    >>> lst_times
    [Time(nome='Flamengo', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='Grêmio', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='São Paulo', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='Corinthians', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='Palmeiras', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0)]
    '''
    ha_time: bool = False
    for i in range(len(lst_times)):
        if lst_times[i].nome == nome:
            ha_time = True
    if ha_time == False:
        lst_times.append(Time(nome, 0, 0, 0, 0, 0, 0, 0))


    # TODO: Arrumar a questão dos jogos e fazer a função
def criterio_ponto(jogo: Jogo, lst_times: list[Time]):
    '''
    A função vai receber uma lista de times *lst_times: list[Time]*,
    vai calcular o criterio de pontos.
    Exemplos:
    >>> lst_times: 
    '''
    anf = jogo.anfitriao
    encontra_nome_time(anf, lst_times)
    vis = jogo.visitante
    encontra_nome_time(vis, lst_times)
    anf_gol = jogo.anf_gol
    vis_gol = jogo.vis_gol
    for i in range(len(lst_times)):
        if lst_times[i].nome == anf:
            if anf_gol > vis_gol:
                lst_times[i].pontos += 3
            elif anf_gol == vis_gol:
                lst_times[i].pontos += 1
        if lst_times[i].nome == vis:
            if vis_gol > anf_gol:
                lst_times[i].pontos += 3
            elif vis_gol == anf_gol:
                lst_times[i].pontos += 1


    # TODO: Fazer a função
def saldo_gol(jogo: Jogo, lst_times: list[Time]):
    '''
    A função vai receber um jogo *jogo: Jogo* e uma lista de times *lst_times: list[Time]*,
    vai calcular o saldo de gols do time.
    Exemplos:
    >>> 

    '''
    for i in range(len(lst_times)):
            ngol_c = lst_times[i].gol_contra
            ngol_m = lst_times[i].gol_marcado
            lst_times[i].saldo_gol = ngol_m - ngol_c


    # TODO: Comentar, Exemplo. Mudar essa, só um exemplo por em quanto *equanto
def quant_gol_time(jogo: Jogo, lst_times: list[Time]) -> None:
    '''
    A função vai receber um jogo *jogo: Jogo* e uma lista de times *lst_times: list[Time]*,
    vai calcular a quantidade de gols marcados pelo anfitriao e pelo visitante.
    Exemplos:
    >>> 

    '''
    anf = jogo.anfitriao
    encontra_nome_time(anf, lst_times)
    vis = jogo.visitante
    encontra_nome_time(vis, lst_times)
    anf_gol = jogo.anf_gol
    vis_gol = jogo.vis_gol
    for i in range(len(lst_times)):
        if lst_times[i].nome == anf:
            lst_times[i].gol_marcado += anf_gol
            lst_times[i].gol_contra += vis_gol
        if lst_times[i].nome == vis:
            lst_times[i].gol_marcado += vis_gol
            lst_times[i].gol_contra += anf_gol
 
    # TODO: Fazer os exemplos da quant_vitorias_time
    # TODO: Corrigir a atualiza_banco vão retornar(None?)

def quant_vitorias_time(jogo: Jogo, lst_times: list[Time]):
    '''
    A função vai receber um jogo *jogo: Jogo* e uma lista de times *lst_times: list[Time]*,
    vai calcular a quantidade de vitorias do time.
    Exemplos:
    >>> jogo = 
    >>> lst_times = [Time('Flamengo', 2, 'Grêmio', 2)]
    >>> lst_times = [Time('Flamengo', 0, 0, 0, 0, 0, 0, 0), Time('Grêmio', 0, 0, 0, 0, 0, 0, 0), Time('Palmeiras', 0, 0, 0, 0, 0, 0, 0)]
    >>> quant_vitorias_time(jogo, lst_times)
    >>> lst_times
    []
    '''
    anf = jogo.anfitriao
    encontra_nome_time(anf, lst_times)
    vis = jogo.visitante
    encontra_nome_time(vis, lst_times)
    anf_gol = jogo.anf_gol
    vis_gol = jogo.vis_gol
    for i in range(len(lst_times)):
        if lst_times[i].nome == anf:
            if anf_gol > vis_gol:
                lst_times[i].vitoria += 1
        if lst_times[i].nome == vis:
            if vis_gol > anf_gol:
                lst_times[i].vitoria += 1


def atualiza_banco(lst_jogos: list[Jogo], lst_times: list[Time], index: int = 0):
    '''
    A função vai receber os jogos *jogo: Jogo* e uma lista de times *lst_times: list[Time]*,
    e vai atualizar o banco de dados.
    '''
    if index >= len(lst_jogos):
        return
    jogo = lst_jogos[index]
    encontra_nome_time(jogo.anfitriao, lst_times)
    encontra_nome_time(jogo.visitante, lst_times)
    atualiza_banco(lst_jogos, lst_times, index + 1)



def sort(lst_times: list[Time]) -> None:
    '''
    '''
    

def aproveitamento_anf(time: Time) -> float:
    '''
    A função vai receber um time *time: Time* e vai calcular o aproveitamento do time.
    Exemplos:
    '''
    return time.anf_pontos / (time.anf_jogos*3)


def melhor_aproveitamento(lst_times: list[Time]) -> None:
    '''
    A função vai receber uma lista de times *lst_times: list[Time]*,
    vai ordenar a lista usando o algoritmo Bubble Sort com base no aproveitamento do time.
    Exemplos:
    
    '''
    n = len(lst_times)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if aproveitamento_anf(lst_times[j]) < aproveitamento_anf(lst_times[j+1]):
                lst_times[j], lst_times[j+1] = lst_times[j+1], lst_times[j]


def melhor_defesa() -> None:
    '''
    '''


def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)

    jogos = le_arquivo(sys.argv[1])

    # TODO: solução da pergunta 1
    # TODO: solução da pergunta 2
    # TODO: solução da pergunta 3

def le_arquivo(nome: str) -> list[str]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento     
    representa uma linha.

    Por exemplo, se o conteúdo do arquivo for
    Sao-Paulo 1 Atletico-MG 2 
    Flamengo 2 Palmeiras 1 

    a resposta produzida é
    [‘Sao-Paulo 1 Atletico-MG 2’, ‘Flamengo 2 Palmeiras 1’]
    '''
    try:
        with open(nome) as f:
            return f.readlines()
           
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)

if __name__ == '__main__':
    main()