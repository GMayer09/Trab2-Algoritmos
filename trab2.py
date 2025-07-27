from dataclasses import dataclass
import sys


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
    anfitriao: Time
    anf_gol: int
    visitante: Time
    vis_gol: int


def encontra_nome_time(time: Time, lst_times: list[Time]) -> None:
    '''
    A função vai receber um nome *nome: Time* e uma lista de times *lst_times: list[Time]*,
    vai verificar se tem um time na lista, caso contrário vai adicionar esse time na lista.
    Exemplos:
    >>> flamengo: Time = Time('Flamengo', 1, 2, 3, 4, 5, 6, 7)
    >>> gremio: Time = Time('Grêmio', 0, 0, 0, 0, 0, 0, 0)
    >>> sao_paulo: Time = Time('São Paulo', 0, 0, 0, 0, 0, 0, 0)
    >>> corinthians: Time = Time('Corinthians', 0, 0, 0, 0, 0, 0, 0)
    >>> palmeiras: Time = Time('Palmeiras', 1, 2, 3, 4, 5, 6, 7)
    >>> lst_times: list[Time] = [flamengo, gremio, sao_paulo, corinthians]
    >>> encontra_nome_time(palmeiras, lst_times)
    >>> lst_times
    [Time(nome='Flamengo', pontos=1, vitoria=2, gol_marcado=3, gol_contra=4, saldo_gol=5, anf_jogos=6, anf_pontos=7), Time(nome='Grêmio', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='São Paulo', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='Corinthians', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='Palmeiras', pontos=1, vitoria=2, gol_marcado=3, gol_contra=4, saldo_gol=5, anf_jogos=6, anf_pontos=7)]
    >>> encontra_nome_time(flamengo, lst_times)
    >>> lst_times
    [Time(nome='Flamengo', pontos=1, vitoria=2, gol_marcado=3, gol_contra=4, saldo_gol=5, anf_jogos=6, anf_pontos=7), Time(nome='Grêmio', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='São Paulo', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='Corinthians', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='Palmeiras', pontos=1, vitoria=2, gol_marcado=3, gol_contra=4, saldo_gol=5, anf_jogos=6, anf_pontos=7)]
    '''
    ha_time: bool = False
    for i in range(len(lst_times)):
        if lst_times[i].nome == time.nome:
            ha_time = True
    if ha_time == False:
        lst_times.append(time)


def criterio_ponto(jogo: Jogo, lst_times: list[Time]):
    '''
    A função vai receber um jogo *jogo: Jogo* e uma lista de times *lst_times: list[Time]*,
    vai calcular o criterio de pontos. ELE NÃO ATUALIZA A QUANTIDADE DE GOLS.
    Exemplos:
    >>> flamengo: Time = Time('Flamengo', 6, 2, 4, 1, 3, 2, 1)
    >>> gremio: Time = Time('Grêmio', 0, 0, 0, 0, 0, 0, 0)
    >>> sao_paulo: Time = Time('São Paulo', 0, 0, 0, 0, 0, 0, 0)
    >>> corinthians: Time = Time('Corinthians', 0, 0, 0, 0, 0, 0, 0)
    >>> jogo1: Jogo = Jogo(flamengo, 0, gremio, 0)
    >>> lst_jogos: list[Jogo] = [jogo1]
    >>> lst_times: list[Time] = [flamengo, gremio, sao_paulo, corinthians]
    >>> atualiza_banco(lst_jogos, lst_times)
    >>> lst_times
    [Time(nome='Flamengo', pontos=7, vitoria=2, gol_marcado=4, gol_contra=1, saldo_gol=3, anf_jogos=3, anf_pontos=2), Time(nome='Grêmio', pontos=1, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='São Paulo', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='Corinthians', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0)]
    '''
    anf = jogo.anfitriao
    vis = jogo.visitante
    anf_gol = jogo.anf_gol
    vis_gol = jogo.vis_gol
    for i in range(len(lst_times)):
        if lst_times[i].nome == anf.nome:
            if anf_gol > vis_gol:
                lst_times[i].pontos += 3
                lst_times[i].anf_pontos += 3
            elif vis_gol == anf_gol:
                lst_times[i].pontos += 1
                lst_times[i].anf_pontos += 1
            lst_times[i].anf_jogos += 1
        elif lst_times[i].nome == vis.nome:
            if vis_gol > anf_gol:
                lst_times[i].pontos += 3
            elif vis_gol == anf_gol:
                lst_times[i].pontos += 1


def saldo_gol(lst_times: list[Time]):
    '''
    A função vai receber uma lista de times *lst_times: list[Time]* e
    vai calcular o saldo de gols do time.
    Exemplos: |O *atualiza_banco* JÁ CHAMA O *saldo_gol*|
    >>> flamengo: Time = Time('Flamengo', 0, 0, 0, 0, 0, 0, 0)
    >>> gremio: Time = Time('Grêmio', 0, 0, 0, 0, 0, 0, 0)
    >>> sao_paulo: Time = Time('São Paulo', 0, 0, 0, 0, 0, 0, 0)
    >>> corinthians: Time = Time('Corinthians', 0, 0, 0, 0, 0, 0, 0)
    >>> jogo1: Jogo = Jogo(flamengo, 2, gremio, 2)
    >>> jogo2: Jogo = Jogo(sao_paulo, 1, corinthians, 2)
    >>> jogo3: Jogo = Jogo(gremio, 2, corinthians, 1)
    >>> jogo4: Jogo = Jogo(flamengo, 1, sao_paulo, 2)
    >>> lst_jogos: list[Jogo] = [jogo1, jogo2, jogo3, jogo4]
    >>> lst_times: list[Time] = [flamengo, gremio, sao_paulo, corinthians]
    >>> atualiza_banco(lst_jogos, lst_times)
    >>> lst_times
    [Time(nome='Flamengo', pontos=1, vitoria=0, gol_marcado=3, gol_contra=4, saldo_gol=-1, anf_jogos=2, anf_pontos=1), Time(nome='Grêmio', pontos=4, vitoria=1, gol_marcado=4, gol_contra=3, saldo_gol=1, anf_jogos=1, anf_pontos=3), Time(nome='São Paulo', pontos=3, vitoria=1, gol_marcado=3, gol_contra=3, saldo_gol=0, anf_jogos=1, anf_pontos=0), Time(nome='Corinthians', pontos=3, vitoria=1, gol_marcado=3, gol_contra=3, saldo_gol=0, anf_jogos=0, anf_pontos=0)]
    '''
    for i in range(len(lst_times)):
            ngol_c = lst_times[i].gol_contra
            ngol_m = lst_times[i].gol_marcado
            lst_times[i].saldo_gol = ngol_m - ngol_c


def quant_gol_time(jogo: Jogo, lst_times: list[Time]) -> None:
    '''
    A função vai receber um jogo *jogo: Jogo* e uma lista de times *lst_times: list[Time]*,
    vai calcular a quantidade de gols marcados pelo anfitriao e pelo visitante.
    Exemplos: |O *atualiza_banco* JÁ CHAMA O *quant_gol_time*|
    >>> flamengo: Time = Time('Flamengo', 0, 0, 0, 0, 0, 0, 0)
    >>> gremio: Time = Time('Grêmio', 0, 0, 0, 0, 0, 0, 0)
    >>> sao_paulo: Time = Time('São Paulo', 0, 0, 0, 0, 0, 0, 0)
    >>> corinthians: Time = Time('Corinthians', 0, 0, 0, 0, 0, 0, 0)
    >>> jogo1: Jogo = Jogo(flamengo, 2, gremio, 2)
    >>> jogo2: Jogo = Jogo(sao_paulo, 1, corinthians, 2)
    >>> jogo3: Jogo = Jogo(gremio, 2, corinthians, 1)
    >>> jogo4: Jogo = Jogo(flamengo, 1, sao_paulo, 2)
    >>> lst_jogos: list[Jogo] = [jogo1, jogo2, jogo3, jogo4]
    >>> lst_times: list[Time] = [flamengo, gremio, sao_paulo, corinthians]
    >>> atualiza_banco(lst_jogos, lst_times)
    >>> lst_times
    [Time(nome='Flamengo', pontos=1, vitoria=0, gol_marcado=3, gol_contra=4, saldo_gol=-1, anf_jogos=2, anf_pontos=1), Time(nome='Grêmio', pontos=4, vitoria=1, gol_marcado=4, gol_contra=3, saldo_gol=1, anf_jogos=1, anf_pontos=3), Time(nome='São Paulo', pontos=3, vitoria=1, gol_marcado=3, gol_contra=3, saldo_gol=0, anf_jogos=1, anf_pontos=0), Time(nome='Corinthians', pontos=3, vitoria=1, gol_marcado=3, gol_contra=3, saldo_gol=0, anf_jogos=0, anf_pontos=0)]
    '''
    anf = jogo.anfitriao
    vis = jogo.visitante
    anf_gol = jogo.anf_gol
    vis_gol = jogo.vis_gol
    for i in range(len(lst_times)):
        if lst_times[i].nome == anf.nome:
            lst_times[i].gol_marcado += anf_gol
            lst_times[i].gol_contra += vis_gol
        if lst_times[i].nome == vis.nome:
            lst_times[i].gol_marcado += vis_gol
            lst_times[i].gol_contra += anf_gol
 

def quant_vitorias_time(jogo: Jogo, lst_times: list[Time]):
    '''
    A função vai receber um jogo *jogo: Jogo* e uma lista de times *lst_times: list[Time]*,
    vai calcular a quantidade de vitorias do time.
    Exemplos: |O *atualiza_banco* JÁ CHAMA O *quant_vitorias_time*|
    >>> flamengo: Time = Time('Flamengo', 0, 0, 0, 0, 0, 0, 0)
    >>> gremio: Time = Time('Grêmio', 0, 0, 0, 0, 0, 0, 0)
    >>> sao_paulo: Time = Time('São Paulo', 0, 0, 0, 0, 0, 0, 0)
    >>> corinthians: Time = Time('Corinthians', 0, 0, 0, 0, 0, 0, 0)
    >>> jogo1: Jogo = Jogo(flamengo, 2, gremio, 2)
    >>> jogo2: Jogo = Jogo(sao_paulo, 1, corinthians, 2)
    >>> jogo3: Jogo = Jogo(gremio, 2, corinthians, 1)
    >>> jogo4: Jogo = Jogo(flamengo, 1, sao_paulo, 2)
    >>> lst_jogos: list[Jogo] = [jogo1, jogo2, jogo3, jogo4]
    >>> lst_times: list[Time] = [flamengo, gremio, sao_paulo, corinthians]
    >>> atualiza_banco(lst_jogos, lst_times)
    >>> lst_times
    [Time(nome='Flamengo', pontos=1, vitoria=0, gol_marcado=3, gol_contra=4, saldo_gol=-1, anf_jogos=2, anf_pontos=1), Time(nome='Grêmio', pontos=4, vitoria=1, gol_marcado=4, gol_contra=3, saldo_gol=1, anf_jogos=1, anf_pontos=3), Time(nome='São Paulo', pontos=3, vitoria=1, gol_marcado=3, gol_contra=3, saldo_gol=0, anf_jogos=1, anf_pontos=0), Time(nome='Corinthians', pontos=3, vitoria=1, gol_marcado=3, gol_contra=3, saldo_gol=0, anf_jogos=0, anf_pontos=0)]
    '''
    anf = jogo.anfitriao
    vis = jogo.visitante
    anf_gol = jogo.anf_gol
    vis_gol = jogo.vis_gol
    for i in range(len(lst_times)):
        if lst_times[i].nome == anf.nome:
            if anf_gol > vis_gol:
                lst_times[i].vitoria += 1
        if lst_times[i].nome == vis.nome:
            if vis_gol > anf_gol:
                lst_times[i].vitoria += 1


def atualiza_banco(lst_jogos: list[Jogo], lst_times: list[Time], index: int = 0):
    '''
    A função vai receber uma lista de jogos *lst_jogos: list[Jogo]*,
    uma lista de times *lst_times: list[Time]* e um index *index: int = 0*,
    e vai atualizar o banco de dados das funções anteriores.
    Exemplos:
    >>> flamengo: Time = Time('Flamengo', 0, 0, 0, 0, 0, 0, 0)
    >>> gremio: Time = Time('Grêmio', 0, 0, 0, 0, 0, 0, 0)
    >>> sao_paulo: Time = Time('São Paulo', 0, 0, 0, 0, 0, 0, 0)
    >>> corinthians: Time = Time('Corinthians', 0, 0, 0, 0, 0, 0, 0)
    >>> jogo1: Jogo = Jogo(flamengo, 2, gremio, 2)
    >>> jogo2: Jogo = Jogo(sao_paulo, 1, corinthians, 2)
    >>> jogo3: Jogo = Jogo(gremio, 2, corinthians, 1)
    >>> jogo4: Jogo = Jogo(flamengo, 1, sao_paulo, 2)
    >>> lst_jogos: list[Jogo] = [jogo1, jogo2, jogo3, jogo4]
    >>> lst_times: list[Time] = [flamengo, gremio, sao_paulo, corinthians]
    >>> atualiza_banco(lst_jogos, lst_times)
    >>> lst_times
    [Time(nome='Flamengo', pontos=1, vitoria=0, gol_marcado=3, gol_contra=4, saldo_gol=-1, anf_jogos=2, anf_pontos=1), Time(nome='Grêmio', pontos=4, vitoria=1, gol_marcado=4, gol_contra=3, saldo_gol=1, anf_jogos=1, anf_pontos=3), Time(nome='São Paulo', pontos=3, vitoria=1, gol_marcado=3, gol_contra=3, saldo_gol=0, anf_jogos=1, anf_pontos=0), Time(nome='Corinthians', pontos=3, vitoria=1, gol_marcado=3, gol_contra=3, saldo_gol=0, anf_jogos=0, anf_pontos=0)]
    '''
    if index >= len(lst_jogos):
        saldo_gol(lst_times)
        return
    jogo = lst_jogos[index]
    encontra_nome_time(jogo.anfitriao, lst_times)
    encontra_nome_time(jogo.visitante, lst_times)
    criterio_ponto(jogo, lst_times)
    quant_gol_time(jogo, lst_times)
    quant_vitorias_time(jogo, lst_times)
    atualiza_banco(lst_jogos, lst_times, index + 1)


def bubble_sort(lst_times: list[Time]) -> None:
    '''
    A função vai receber uma lista de times *lst_times: list[Time]*,
    vai ordenar usando o algoritmo Bubble Sort.
    Exemplos:
    >>> flamengo: Time = Time('Flamengo', 0, 0, 0, 0, 0, 0, 0)
    >>> gremio: Time = Time('Grêmio', 0, 0, 0, 0, 0, 0, 0)
    >>> sao_paulo: Time = Time('São Paulo', 0, 0, 0, 0, 0, 0, 0)
    >>> corinthians: Time = Time('Corinthians', 0, 0, 0, 0, 0, 0, 0)
    >>> jogo1: Jogo = Jogo(flamengo, 2, gremio, 2)
    >>> jogo2: Jogo = Jogo(sao_paulo, 1, corinthians, 2)
    >>> jogo3: Jogo = Jogo(gremio, 2, corinthians, 1)
    >>> jogo4: Jogo = Jogo(flamengo, 1, sao_paulo, 2)
    >>> lst_jogos: list[Jogo] = [jogo1, jogo2, jogo3, jogo4]
    >>> lst_times: list[Time] = [flamengo, gremio, sao_paulo, corinthians]
    >>> atualiza_banco(lst_jogos, lst_times)
    >>> bubble_sort(lst_times)
    >>> lst_times
    [Time(nome='Grêmio', pontos=4, vitoria=1, gol_marcado=4, gol_contra=3, saldo_gol=1, anf_jogos=1, anf_pontos=3), Time(nome='São Paulo', pontos=3, vitoria=1, gol_marcado=3, gol_contra=3, saldo_gol=0, anf_jogos=1, anf_pontos=0), Time(nome='Corinthians', pontos=3, vitoria=1, gol_marcado=3, gol_contra=3, saldo_gol=0, anf_jogos=0, anf_pontos=0), Time(nome='Flamengo', pontos=1, vitoria=0, gol_marcado=3, gol_contra=4, saldo_gol=-1, anf_jogos=2, anf_pontos=1)]
    '''
    n = len(lst_times)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst_times[j].pontos < lst_times[j+1].pontos:
                lst_times[j], lst_times[j+1] = lst_times[j+1], lst_times[j]
            elif lst_times[j].pontos == lst_times[j+1].pontos:
                if lst_times[j].vitoria < lst_times[j+1].vitoria:
                    lst_times[j], lst_times[j+1] = lst_times[j+1], lst_times[j]
                elif lst_times[j].vitoria == lst_times[j+1].vitoria:
                    if lst_times[j].saldo_gol < lst_times[j+1].saldo_gol:
                        lst_times[j], lst_times[j+1] = lst_times[j+1], lst_times[j]
                    elif lst_times[j].saldo_gol == lst_times[j+1].saldo_gol:
                        if lst_times[j].nome < lst_times[j+1].nome:
                            lst_times[j], lst_times[j+1] = lst_times[j+1], lst_times[j]


def aproveitamento_anf(time: Time) -> float:
    '''
    A função vai receber um time *time: Time*, vai calcular o aproveitamento do time
    e vai retornar um float com o valor do aproveitamento.
    Exemplos:
    >>> flamengo: Time = Time('Flamengo', 0, 0, 0, 0, 0, 3, 7)
    >>> gremio: Time = Time('Grêmio', 0, 0, 0, 0, 0, 49, 133)
    >>> aproveitamento_anf(flamengo)
    0.7777777777777778
    >>> aproveitamento_anf(gremio)
    0.9047619047619048
    '''
    if time.anf_jogos == 0:
        return 0.0
    return time.anf_pontos / (time.anf_jogos*3)


def melhor_aproveitamento(lst_times: list[Time]) -> None:
    '''
    A função vai receber uma lista de times *lst_times: list[Time]*,
    vai ordenar a lista usando o algoritmo Bubble Sort com base no aproveitamento do time.
    Exemplos:
    >>> flamengo: Time = Time('Flamengo', 0, 0, 0, 0, 0, 2, 1)
    >>> gremio: Time = Time('Grêmio', 0, 0, 0, 0, 0, 1, 3)
    >>> sao_paulo: Time = Time('São Paulo', 0, 0, 0, 0, 0, 1, 0)
    >>> corinthians: Time = Time('Corinthians', 0, 0, 0, 0, 0, 0, 0)
    >>> lst_times = [flamengo, gremio, sao_paulo, corinthians]
    >>> melhor_aproveitamento(lst_times)
    >>> lst_times
    [Time(nome='Grêmio', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=1, anf_pontos=3), Time(nome='Flamengo', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=2, anf_pontos=1), Time(nome='São Paulo', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=1, anf_pontos=0), Time(nome='Corinthians', pontos=0, vitoria=0, gol_marcado=0, gol_contra=0, saldo_gol=0, anf_jogos=0, anf_pontos=0)]
    '''
    n = len(lst_times)
    lst_nova = []
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if aproveitamento_anf(lst_times[j]) < aproveitamento_anf(lst_times[j+1]):
                lst_times[j], lst_times[j+1] = lst_times[j+1], lst_times[j]


def print_melhor_aproveitamento(lst_times: list[Time]) -> None:
    '''
    A função vai receber uma lista de times *lst_times: list[Time]* e vai imprimir os melhores aproveitamentos.
    Calculando o a mediana *mid_point* e criando uma lista só com os valores de aproveitamento maiores que a mediana.
    '''
    lst_nova = []
    mid_point = 0.0
    _max = 0.0
    _min = 0.0
    for time in lst_times:
        if aproveitamento_anf(time) > _max:
            _max = aproveitamento_anf(time)
        if aproveitamento_anf(time) < _min:
            _min = aproveitamento_anf(time)
    mid_point = (_max + _min) / 2
    for time in lst_times:
        if aproveitamento_anf(time) >= mid_point:
            lst_nova.append(time)
    melhor_aproveitamento(lst_nova)
    print("Melhor Aproveitamento afitrião:")
    for time in lst_nova:
        print(f"{time.nome}: {int(aproveitamento_anf(time) * 100)}%")



def melhor_defesa(lst_times: list[Time]) -> list[Time]:
    '''
    A função vai receber um lista de times *lst_times: list[Time]*,
    vai ordenar usando recursão e retornar a lista dos times com a melhor defesa.
    Exemplos:
    >>> flamengo: Time = Time('Flamengo', 0, 0, 0, 0, 0, 0, 0)
    >>> gremio: Time = Time('Grêmio', 0, 0, 0, 0, 0, 0, 0)
    >>> sao_paulo: Time = Time('São Paulo', 0, 0, 0, 0, 0, 0, 0)
    >>> corinthians: Time = Time('Corinthians', 0, 0, 0, 0, 0, 0, 0)
    >>> jogo1: Jogo = Jogo(flamengo, 2, gremio, 2)
    >>> jogo2: Jogo = Jogo(sao_paulo, 1, corinthians, 2)
    >>> jogo3: Jogo = Jogo(gremio, 2, corinthians, 1)
    >>> jogo4: Jogo = Jogo(flamengo, 1, sao_paulo, 2)
    >>> lst_jogos: list[Jogo] = [jogo1, jogo2, jogo3, jogo4]
    >>> lst_times: list[Time] = [flamengo, gremio, sao_paulo, corinthians]
    >>> atualiza_banco(lst_jogos, lst_times)
    >>> melhor_defesa(lst_times)
    [Time(nome='Grêmio', pontos=4, vitoria=1, gol_marcado=4, gol_contra=3, saldo_gol=1, anf_jogos=1, anf_pontos=3), Time(nome='São Paulo', pontos=3, vitoria=1, gol_marcado=3, gol_contra=3, saldo_gol=0, anf_jogos=1, anf_pontos=0), Time(nome='Corinthians', pontos=3, vitoria=1, gol_marcado=3, gol_contra=3, saldo_gol=0, anf_jogos=0, anf_pontos=0)]
    '''
    if len(lst_times) <= 1:
        return lst_times

    melhores_times_resto = melhor_defesa(lst_times[1:])

    primeiro_time = lst_times[0]
    gols_sofridos_melhor_defesa = melhores_times_resto[0].gol_contra

    if primeiro_time.gol_contra < gols_sofridos_melhor_defesa:
        return [primeiro_time]
    elif primeiro_time.gol_contra == gols_sofridos_melhor_defesa:
        return [primeiro_time] + melhores_times_resto
    else:
        return melhores_times_resto


def conv_lst_jogos(lst: list[str]) -> list[Jogo]:
    '''
    A função vai receber uma lista *lst: list[str]*,
    '''
    lst_jogos = []

    for s in lst:
        s_clean = ""
        i = 0
        while i < len(s):
            if s[i] != '\n' and not (s[i] == ' ' and (i == len(s)-1 or s[i+1] == ' ' or s[i+1] == '\n')):
                s_clean += s[i]
            i += 1
        
        space_indices = []
        for i in range(len(s_clean)):
            if s_clean[i] == ' ':
                space_indices.append(i)
        
        anf_name = ""
        for i in range(space_indices[0]):
            anf_name += s_clean[i]
        
        anf_gol_str = ""
        for i in range(space_indices[0] + 1, space_indices[1]):
            anf_gol_str += s_clean[i]
        anf_gol = int(anf_gol_str)
        
        vis_name = ""
        for i in range(space_indices[1] + 1, space_indices[2]):
            vis_name += s_clean[i]
        
        vis_gol_str = ""
        for i in range(space_indices[2] + 1, len(s_clean)):
            vis_gol_str += s_clean[i]
        vis_gol = int(vis_gol_str)
        
        jogo = Jogo(anfitriao=Time(anf_name, 0, 0, 0, 0, 0, 0, 0), anf_gol=anf_gol, visitante=Time(vis_name, 0, 0, 0, 0, 0, 0, 0), vis_gol=vis_gol)
        lst_jogos.append(jogo)
    
    return lst_jogos


def len_max(lst: list[Time]) -> int:
    '''
    A função vai receber uma lista *lst: list[str]*,
    vai retornar o tamanho da maior string da lista.
    Exemplos:
    '''
    max_len = 0
    for time in lst:
        if len(time.nome) > max_len:
            max_len = len(time.nome)
    return max_len


def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)

    jogos = le_arquivo(sys.argv[1])
    lst_times = []
    lst_jogos = conv_lst_jogos(jogos)
    atualiza_banco(lst_jogos, lst_times)

    # solução da pergunta 1
    bubble_sort(lst_times)
    print("Classficação do Brasileirão:")

    max_len = len_max(lst_times)
    print(f"TIME{' ' * (max_len - 3)}P   V   S")
    for time in lst_times:
        if time.pontos >= 10:
            print(f"{time.nome}{' ' * (max_len - len(time.nome) + 1)}{time.pontos}  {time.vitoria}   {time.saldo_gol}")
        else:
            print(f"{time.nome}{' ' * (max_len - len(time.nome) + 1)}{time.pontos}   {time.vitoria}   {time.saldo_gol}")
    print('\n')
    
    # solução da pergunta 2
    print_melhor_aproveitamento(lst_times)
    print('\n')

    # solução da pergunta 3
    lst_nova = melhor_defesa(lst_times)
    print("Melhor defesa:")
    max_len = len_max(lst_nova)
    print(f"TIME{' ' * (max_len - 3)}P   V   S")
    for time in lst_nova:
        print(f"{time.nome}{' ' * (max_len - len(time.nome) + 1)}{time.pontos}   {time.vitoria}   {time.saldo_gol}")
    


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