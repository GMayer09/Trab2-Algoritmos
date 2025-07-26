'''
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
>>>
>>> lst_times
[]
'''