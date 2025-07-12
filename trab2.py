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
    nome, pontos, vitoria, empate, derrota, gol_marcado, gol_contra.
    '''
    nome: str
    pontos: int
    vitoria: int
    gol_marcado: int
    gol_contra: int
    anf: bool


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
    >>> lst_times: list[Time] = [Time('Flamengo', 'Grêmio', 'Palmeiras')]
    >>> encontra_nome_time('Flamengo', lst_times)
    [Time('Flamengo', 'Grêmio', 'Palmeiras')]
    >>> encontra_nome_time('Internacional', lst_times)
    [Time('Flamengo', 'Grêmio', 'Palmeiras', 'Internacional')]
    >>> encontra_nome_time('Grêmio', lst_times)
    [Time('Flamengo', 'Grêmio', 'Palmeiras', 'Internacional')]
    '''
    for i in range(len(lst_times)):
        if lst_times[i].nome == nome:
            lst_times.append(Time(nome, 0, 0, 0, 0, 0, 0, 0, 0))

    # TODO: Arrumar a questão dos jogos e fazer a função
def criterios(lst_times: list[Time], lst_jogos: list[Jogo], criterio: CriterioDesempate) -> list[Time]:
    '''
    A função vai receber um jogo *jogo: Jogo* e criterio *criterio: CriterioDesempate*,
    vai calcular a tabela dos times em relação aos jogos 
    Exemplos:
    
    '''
    i: int = 0
    anfiGol = lst_jogos.anf_gol
    visGol = lst_jogos.vis_gol
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

    # TODO: Fazer a função
def saldo_gol(jogo: Jogo, lst_times: list[Time]):
    '''
    A função vai calcular o saldo de gols dos times.
    '''
    for i in range(len(lst_times)):
            ngol_c = lst_times[i].gol_contra
            ngol_m = lst_times[i].gol_marcado
            lst_times[i].saldo_gol = ngol_m - ngol_c


    # TODO: Comentar, Exemplo. Mudar essa, só um exemplo por em quanto *equanto
def quant_gol_time(jogo: Jogo, lst_times: list[Time]) -> None:
    '''
    A função vai receber um jogo *jogo: Jogo* e uma lista de times *lst_times: list[Time]*,

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

    # TODO: Fazer funções de: Quantificar as vitorias
    # TODO: Ver o que as funções quant_vitorias_time e atualiza_banco vão retornar(None?)

def quant_vitorias_time(jogo: Jogo, lst_times: list[Time]):
    '''
    
    '''


def atualiza_banco(jogo: Jogo, lst_times: list[Time]):
    '''
    A função vai receber os jogos *jogo: Jogo* e uma lista de times *lst_times: list[Time]*,
    e vai atualizar o banco de dados.
    '''
    for i in lst_times:
        anf = jogo.anfitriao
        encontra_nome_time(anf, lst_times)
        vis = jogo.visitante
        encontra_nome_time(vis, lst_times)



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