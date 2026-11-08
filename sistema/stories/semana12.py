import json
G=lambda t:f"<span class='gold'>{t}</span>"
S='sistema/stories/src/'; P='posts/consultoria/'
I=[
# 08 dom
dict(d='2026-11-08',h='10:00',t='pessoal',img=S+'pes1.jpg',title=f"Domingo é dia de {G('recarregar')}"),
dict(d='2026-11-08',h='19:30',t='novo',img=P+'096/01.jpg',title='Pare de comer só frango'),
# 09 seg
dict(d='2026-11-09',h='10:00',t='resultado',img=S+'res1.jpg',title=f"Shape de {G('palco')}",text='Preparação com estratégia, ajustada semana a semana pelo feedback.'),
dict(d='2026-11-09',h='12:30',t='novo_reel',title=f"Overall {G('Classic')}",text='Mais um título na conta. O trampo continua sendo feito.'),
# 10 ter
dict(d='2026-11-10',h='10:00',t='dica',title=f"Deload {G('não é fraqueza')}",items=['Cansaço que não passa? Seu corpo está pedindo pausa','Reduza volume e carga por 1 semana','Volte mais forte e sem lesão']),
dict(d='2026-11-10',h='19:30',t='novo',img=P+'160/01.jpg',title='Estreia com overall'),
# 11 qua
dict(d='2026-11-11',h='10:00',t='bastidor',img=S+'bast1.jpg',title=f"Acompanhamento {G('de perto')}"),
dict(d='2026-11-11',h='19:30',t='novo',img=P+'266/01.jpg',title='Consultoria sem fronteiras'),
# 12 qui
dict(d='2026-11-12',h='10:00',t='prova',img=S+'prova1.jpg',title=f"Suporte {G('de verdade')}"),
dict(d='2026-11-12',h='12:30',t='novo_reel',title=f"Back Off {G('Set')}",text='4 séries pesadas + 1 série leve até a falha. Veja como aplicar.'),
# 13 sex
dict(d='2026-11-13',h='10:00',t='chamada',title=f"Vagas {G('abertas')}",text='Treino, dieta e acompanhamento ajustados pelo seu feedback. 100% online.'),
dict(d='2026-11-13',h='19:30',t='novo',img=P+'232/01.jpg',title='Primeiro campeonato, três pódios'),
# 14 sab
dict(d='2026-11-14',h='10:00',t='arquivo',img=S+'arq1.jpg',year='Era dos fóruns',title=f"Antes do Instagram, {G('já era treino')}"),
dict(d='2026-11-14',h='19:30',t='novo',img=P+'073/01.jpg',title='Fome à noite não é compulsão'),
# 15 dom
dict(d='2026-11-15',h='10:00',t='pessoal',img=S+'pes2.jpg',title=f"O trabalho me {G('levou longe')}"),
dict(d='2026-11-15',h='12:30',t='novo_reel',title=f"Monster {G('Cast')}",text='Participação no Monster Cast. Corte novo no perfil.'),
# 16 seg
dict(d='2026-11-16',h='10:00',t='resultado',img=S+'res2.jpg',title=f"Medalha no {G('peito')}",text='Resultado não é sorte. É método aplicado com consistência.'),
dict(d='2026-11-16',h='19:30',t='novo',img=P+'334/01.jpg',title='3 realidades, 1 objetivo'),
# 17 ter
dict(d='2026-11-17',h='10:00',t='dica',title=f"Peso na balança {G('engana')}",items=['Compare fotos, não só o número','Mesmo peso pode ser outro físico','Medidas e espelho contam a história']),
dict(d='2026-11-17',h='19:30',t='novo',img=P+'024/01.jpg',title='Confie no seu treinador'),
# 18 qua
dict(d='2026-11-18',h='10:00',t='bastidor',img=P+'203/01.jpg',title=f"Autoridade vem {G('com o tempo')}"),
dict(d='2026-11-18',h='12:30',t='novo_reel',title=f"Top 1 {G('Classic')}",text='Mais um aluno no topo do pódio. O segredo? Assiste lá.'),
# 19 qui
dict(d='2026-11-19',h='10:00',t='prova',img=S+'prova2.jpg',title=f"Nunca vi isso {G('em consultoria')}"),
dict(d='2026-11-19',h='19:30',t='novo',img=P+'357/01.jpg',title='Um casal, dois campeões'),
# 20 sex
dict(d='2026-11-20',h='10:00',t='chamada',title=f"Seu {G('melhor físico')}",text='Atleta ou não, a estratégia se adapta à sua rotina. Comece agora.'),
dict(d='2026-11-20',h='19:30',t='novo',img=P+'260/01.jpg',title='Eu rasguei meu peito'),
# 21 sab
dict(d='2026-11-21',h='10:00',t='arquivo',img=S+'arq2.jpg',year='TBT',title=f"Muito antes {G('do celular')}"),
dict(d='2026-11-21',h='12:30',t='novo_reel',title=f"Trabalho {G('no OFF')}",text='Bastidores de uma preparação. Quer mais conteúdo assim?'),
]
for i in I: i['name']=f"{i['d'][5:].replace('-','')}_{i['h'].replace(':','')}_{i['t']}"
json.dump(I,open('semana12.json','w'),ensure_ascii=False,indent=1)
print(len(I))
