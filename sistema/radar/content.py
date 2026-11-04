# Conteúdo dos 15 posts do @radar_fitnessbr
HANDLE = "@radar_fitnessbr"

TAGS_BASE = "#hyrox #crossfit #fitness #treinohibrido #educacaofisica #tecnologoemeducacaofisica"
TAGS_CARREIRA = "#tecnologoemeducacaofisica #tecnologoemmusculacao #educacaofisica #profissionaldeeducacaofisica #personaltrainer #carreirafitness"

POSTS = [
# 1
dict(id="01", fmt="C", slides=[
  dict(k="cover", tag="HYROX", title="O que é HYROX e por que todo mundo está falando disso", sub="Arrasta →"),
  dict(k="point", n="01", title="A prova é sempre a mesma", body="8 × (1 km de corrida + 1 estação). Em qualquer cidade do mundo, o percurso é idêntico. Por isso dá pra comparar o seu tempo com o de qualquer atleta."),
  dict(k="list", title="As 8 estações", items=["SkiErg 1.000 m","Sled Push 50 m","Sled Pull 50 m","Burpee Broad Jump 80 m","Remo 1.000 m","Farmers Carry 200 m","Sandbag Lunges 100 m","Wall Balls 100 reps"]),
  dict(k="stat", big="+570", title="academias afiliadas no Brasil", body="As buscas por HYROX no país cresceram 330% em um ano. A expectativa é de 30 mil atletas na temporada 2026/27."),
  dict(k="point", n="04", title="Por que explodiu", body="Qualquer pessoa consegue terminar. Não exige ginástica olímpica nem LPO. E tem chegada, medalha e ranking — vira meta de treino de verdade."),
  dict(k="cta", title="Você já correu uma HYROX?", body="Conta aqui nos comentários. E segue o Radar pra acompanhar tudo do treino híbrido."),
], caption="""HYROX não é moda passageira. É o formato de competição fitness que mais cresce no mundo — e o Brasil já tem mais de 570 academias afiliadas.

O segredo é simples: a prova é sempre igual. 8 km de corrida intercalados com 8 estações. Dá pra medir evolução, comparar tempo e treinar com objetivo.

E com o crescimento vem uma pergunta que pouca gente faz: quem está preparando esses atletas? Esse é um assunto que vamos trazer muito aqui.

Salva esse post e manda pra quem está pensando em fazer a primeira prova.

""" + TAGS_BASE + " #hyroxbrasil #corrida"),

# 2
dict(id="02", fmt="P", slides=[
  dict(k="news", tag="AGENDA", kicker="21–22 NOV · RIOCENTRO", title="HYROX Rio de Janeiro deve ser o maior evento da modalidade no Brasil", body="Expectativa de 10 mil atletas, 30% vindos de outros países."),
], caption="""📍 HYROX Rio de Janeiro — 21 e 22 de novembro, no Riocentro.

A expectativa da organização é reunir 10 mil atletas, com cerca de 30% vindos de fora do país. Se confirmar, vai ser o maior evento da modalidade já feito no Brasil.

Vai correr ou vai assistir? Marca aqui quem vai com você 👇

Fonte: divulgação HYROX/Amazon (Mercado & Consumo, out/2026).

""" + TAGS_BASE + " #hyroxrio #riodejaneiro"),

# 3
dict(id="03", fmt="C", slides=[
  dict(k="cover", tag="COMPARATIVO", title="HYROX x CrossFit: as diferenças que ninguém explica direito", sub="Arrasta →"),
  dict(k="versus", title="O formato", a=("HYROX","Prova fixa. Você sabe exatamente o que vai fazer no dia."), b=("CROSSFIT","Provas variadas. Muitas são reveladas pouco antes da competição.")),
  dict(k="versus", title="A técnica", a=("HYROX","Movimentos simples. O limite é motor e resistência."), b=("CROSSFIT","Exige ginástica, LPO e habilidade. A técnica define o resultado.")),
  dict(k="versus", title="O treino", a=("HYROX","Muita corrida + força resistente. Base aeróbica manda."), b=("CROSSFIT","Força, potência, ginástica e condicionamento. Tudo junto.")),
  dict(k="point", n="✓", title="Qual é melhor?", body="Nenhum. São esportes diferentes. O que importa é o treino ser montado para o objetivo — e isso exige alguém que entenda de fisiologia e periodização."),
  dict(k="cta", title="Time HYROX ou time CrossFit?", body="Comenta aí. Segue o Radar pra mais comparativos."),
], caption="""HYROX e CrossFit vivem sendo colocados no mesmo saco. Mas são esportes bem diferentes.

HYROX: prova fixa, movimentos simples, decide quem tem mais motor.
CrossFit: provas variadas, técnica complexa, decide quem é mais completo.

Nenhum é melhor. O que muda é o treino. E aqui está o ponto: um atleta de HYROX treinado como crossfiteiro (ou o contrário) deixa muito resultado na mesa.

Time HYROX ou time CrossFit? 👇

""" + TAGS_BASE),

# 4
dict(id="04", fmt="P", slides=[
  dict(k="news", tag="CROSSFIT GAMES", kicker="20ª EDIÇÃO · SAN JOSE (EUA)", title="James Sprague e Aimee Cringle são os campeões dos CrossFit Games 2026", body="CrossFit Whip virou no último dia e levou o título por equipes."),
], caption="""🏆 CrossFit Games 2026 — 20ª edição, em San Jose (Califórnia).

👉 Masculino: James Sprague, que reconquista o título.
👉 Feminino: Aimee Cringle, primeiro título dela.
👉 Equipes: CrossFit Whip, que passou a Mayhem no último dia.

Foram 20 provas no individual, a edição com mais eventos da história dos Games.

Você acompanhou? Quem foi o destaque pra você?

""" + TAGS_BASE + " #crossfitgames"),

# 5
dict(id="05", fmt="C", slides=[
  dict(k="cover", tag="HYROX", title="5 erros de quem vai para a primeira HYROX", sub="O nº 3 é o mais comum →"),
  dict(k="point", n="01", title="Sair rápido demais no 1º km", body="A adrenalina engana. Quem passa o primeiro km 20 segundos mais rápido que o planejado paga isso nas últimas estações."),
  dict(k="point", n="02", title="Não treinar o sled", body="Sled push e pull dependem muito do piso e da técnica. Quem nunca empurrou um trenó pesado descobre isso na prova."),
  dict(k="point", n="03", title="Treinar corrida descansado", body="Na prova você corre com as pernas destruídas. Inclua corrida logo depois de exercício de força no treino."),
  dict(k="point", n="04", title="Esquecer o fim da prova", body="Lunges e wall balls chegam quando você já está no limite. É ali que mais gente perde tempo."),
  dict(k="point", n="05", title="Ignorar as transições", body="A Roxzone (área de transição) conta no tempo. Saber onde fica cada estação economiza minutos."),
  dict(k="cta", title="Salva pra revisar antes da prova", body="E manda pro seu parceiro de doubles."),
], caption="""Primeira HYROX chegando? Esses 5 erros custam minutos — e às vezes a prova inteira.

O mais comum: treinar corrida sempre descansado. Na prova, você corre depois de empurrar trenó, remar e carregar peso. O treino precisa simular isso.

Uma preparação bem montada leva em conta o que a prova exige de verdade. É aí que faz diferença ter quem entende de treinamento.

Salva e manda pro seu parceiro de doubles 👊

""" + TAGS_BASE + " #hyroxtraining"),

# 6
dict(id="06", fmt="C", slides=[
  dict(k="cover", tag="CIÊNCIA", title="Treino híbrido: dá pra ganhar força e resistência ao mesmo tempo?", sub="Arrasta →"),
  dict(k="point", n="01", title="O famoso efeito de interferência", body="Treinar aeróbico e força juntos pode atrapalhar alguns ganhos de força e potência. É real — mas menor do que se dizia."),
  dict(k="point", n="02", title="Hipertrofia sofre pouco", body="Para ganho de massa muscular, a interferência tende a ser pequena quando volume e recuperação estão bem ajustados."),
  dict(k="point", n="03", title="O que reduz a interferência", body="Separar as sessões por algumas horas, ajustar o volume de corrida e priorizar a qualidade de cada treino."),
  dict(k="point", n="04", title="Conclusão", body="Dá, sim. Mas não é só somar treino de musculação com treino de corrida. Precisa de periodização."),
  dict(k="cta", title="Você faz treino híbrido?", body="Conta como organiza a sua semana nos comentários."),
], caption="""Força ou resistência? No treino híbrido, a resposta é: as duas — desde que o treino seja bem estruturado.

O efeito de interferência existe, mas é menor do que muita gente pensa, principalmente para hipertrofia. O problema aparece quando a pessoa só empilha treino sem planejamento.

Treino híbrido virou tendência com HYROX e CrossFit. E a demanda por profissional que saiba montar isso só cresce.

Como você organiza sua semana? 👇

""" + TAGS_BASE + " #ciencianotreino"),

# 7
dict(id="07", fmt="P", slides=[
  dict(k="news", tag="RESULTADO", kicker="HYROX SÃO PAULO · OUT/2026", title="Brasileiro Bruno Henrique Silva Carvalho vence o Pro masculino em casa", body="No feminino, título da espanhola Manuela Garcia Caparros."),
], caption="""🇧🇷 Vitória em casa no HYROX São Paulo (17–18 de outubro).

Bruno Henrique Silva Carvalho venceu a categoria Pro masculina. No feminino, a espanhola Manuela Garcia Caparros levou o título com folga.

O nível dos atletas brasileiros está subindo rápido. E isso puxa junto a necessidade de preparação mais profissional.

Deixa um 🔥 pro campeão!

""" + TAGS_BASE + " #hyroxsaopaulo"),

# 8
dict(id="08", fmt="C", slides=[
  dict(k="cover", tag="MERCADO", title="O mercado fitness no Brasil em números", sub="E o que isso significa pra quem trabalha na área →"),
  dict(k="stat", big="~60 mil", title="academias com CNPJ ativo em 2025", body="Em 2015 eram cerca de 22,5 mil. O número quase triplicou em 10 anos."),
  dict(k="stat", big="70 mil", title="é a projeção para 2027", body="Segundo o Panorama Setorial Fitness Brasil."),
  dict(k="stat", big="R$ 20 bi", title="por ano", body="É o quanto o setor movimenta, segundo o Sebrae."),
  dict(k="point", n="→", title="O que isso significa", body="Mais academias, mais modalidades (HYROX, CrossFit, híbrido) e mais exigência. O mercado vai precisar de profissionais com formação específica."),
  dict(k="cta", title="Você trabalha ou quer trabalhar com fitness?", body="Segue o Radar. Vamos falar muito sobre carreira aqui."),
], caption="""O Brasil está entre os maiores mercados fitness do mundo. E não para de crescer.

Eram cerca de 22,5 mil academias em 2015. Em 2025, já passavam de 60 mil — e a projeção é chegar a 70 mil até 2027.

Mais academias significa mais vagas. Mas também mais concorrência. Quem tiver formação específica vai sair na frente.

Você trabalha ou quer trabalhar na área? Conta aí 👇

Fontes: Panorama Setorial Fitness Brasil / Jornal da USP; Sebrae.

#mercadofitness #academia """ + TAGS_CARREIRA),

# 9
dict(id="09", fmt="C", slides=[
  dict(k="cover", tag="CARREIRA", title="Quem está treinando os atletas de HYROX e CrossFit?", sub="Uma pergunta incômoda →"),
  dict(k="point", n="01", title="O esporte cresceu mais rápido que os treinadores", body="Muita gente prescreve treino de alto rendimento copiando planilha da internet."),
  dict(k="point", n="02", title="Alto rendimento exige base", body="Fisiologia do exercício, biomecânica, periodização e avaliação física. Sem isso, o atleta estagna ou se machuca."),
  dict(k="point", n="03", title="O mercado já está separando", body="Atletas e academias afiliadas querem treinador com formação e resultado comprovado."),
  dict(k="point", n="04", title="Formação é diferencial", body="Graduação, tecnólogo ou especialização: quem estuda a área específica se destaca."),
  dict(k="cta", title="Você treina atletas?", body="Segue o Radar. Na próxima semana: as formações que existem no fitness."),
], caption="""O HYROX e o CrossFit cresceram rápido demais. Os treinadores qualificados, nem tanto.

Hoje tem muito atleta treinando com planilha copiada. Funciona até a primeira lesão ou o primeiro platô.

Alto rendimento exige fisiologia, biomecânica e periodização. E o mercado já está percebendo a diferença entre quem estudou e quem improvisa.

Nos próximos posts vamos falar das formações que existem — inclusive as que pouca gente conhece, como o tecnólogo.

""" + TAGS_CARREIRA + " #hyrox #crossfit"),

# 10
dict(id="10", fmt="P", slides=[
  dict(k="poll", tag="ENQUETE", title="Se tivesse que escolher uma prova pra fazer em 2027:", a="HYROX", b="CROSSFIT"),
], caption="""Só pode escolher uma 👇

🅰️ HYROX
🅱️ CrossFit

Comenta A ou B e diz por quê.

""" + TAGS_BASE),

# 11
dict(id="11", fmt="C", slides=[
  dict(k="cover", tag="CARREIRA", title="Profissões no fitness além de personal trainer", sub="Arrasta →"),
  dict(k="point", n="01", title="Treinador de atletas", body="Preparação para competições como HYROX, CrossFit, fisiculturismo e corrida."),
  dict(k="point", n="02", title="Coach online", body="Consultoria a distância, com alunos em qualquer cidade (ou país)."),
  dict(k="point", n="03", title="Especialista em musculação", body="Prescrição de treino de força e hipertrofia para todos os públicos."),
  dict(k="point", n="04", title="Coordenação técnica", body="Responsável pela metodologia e pela equipe de uma academia ou box."),
  dict(k="list", title="Os caminhos de formação", items=["Bacharelado em Educação Física","Licenciatura em Educação Física","Tecnólogo (formação superior focada)","Pós-graduação / especialização"]),
  dict(k="cta", title="Qual dessas você quer seguir?", body="Comenta aí. No próximo post: o que é um tecnólogo."),
], caption="""Educação física não é só dar aula em academia.

Treinador de atletas, coach online, especialista em musculação, coordenador técnico… e cada caminho pede uma formação diferente.

Uma que pouca gente conhece é o tecnólogo: uma graduação superior mais curta e focada numa área específica. Vamos explicar no próximo post.

Qual desses caminhos é o seu? 👇

""" + TAGS_CARREIRA),

# 12
dict(id="12", fmt="C", slides=[
  dict(k="cover", tag="CARREIRA", title="Tecnólogo em educação física: o que é?", sub="Tira as dúvidas →"),
  dict(k="point", n="01", title="É graduação de nível superior", body="O curso tecnológico é uma graduação registrada no MEC, como bacharelado e licenciatura."),
  dict(k="point", n="02", title="É mais curto", body="Os cursos tecnológicos costumam durar de 2 a 3 anos, contra 4 anos de um bacharelado."),
  dict(k="point", n="03", title="É focado", body="Em vez de cobrir tudo, aprofunda numa área. Ex.: Tecnólogo em Musculação e Fisiculturismo."),
  dict(k="point", n="04", title="Pra quem faz sentido", body="Pra quem já sabe em que área quer atuar e quer formação superior com foco prático."),
  dict(k="point", n="!", title="Antes de se matricular", body="Confira o registro do curso no e-MEC e as regras de atuação profissional da área escolhida."),
  dict(k="cta", title="Ficou alguma dúvida?", body="Manda nos comentários que a gente responde."),
], caption="""Tecnólogo em educação física: você sabe o que é?

É uma graduação superior, registrada no MEC, mais curta e mais focada que o bacharelado. Em vez de estudar tudo, você aprofunda na área em que quer atuar.

Um exemplo é o Tecnólogo em Musculação e Fisiculturismo, voltado para treino de força, hipertrofia e preparação de atletas.

Dica importante: antes de se matricular em qualquer curso, consulte o registro no e-MEC.

Dúvidas? Comenta aqui 👇

""" + TAGS_CARREIRA + " #graduacao #ensinosuperior"),

# 13
dict(id="13", fmt="P", slides=[
  dict(k="news", tag="NEGÓCIOS", kicker="PARCERIA GLOBAL", title="Amazon fecha parceria com a HYROX e terá loja dedicada no Brasil", body="Ativações nos eventos de São Paulo e Rio de Janeiro."),
], caption="""💼 A Amazon fechou uma parceria global com a HYROX.

No Brasil, o acordo prevê ativações nos eventos de São Paulo e Rio de Janeiro e uma loja dedicada na Amazon.com.br. Lá fora, a Amazon é patrocinadora principal da HYROX London.

Quando gigantes desse tamanho entram, é sinal de que a modalidade veio pra ficar — e de que o mercado em volta dela (equipamento, eventos, treinadores) vai crescer junto.

Fonte: Mercado & Consumo, out/2026.

""" + TAGS_BASE + " #negociosfitness"),

# 14
dict(id="14", fmt="C", slides=[
  dict(k="cover", tag="CARREIRA", title="Como virar treinador de alto rendimento", sub="O caminho em 5 passos →"),
  dict(k="point", n="01", title="Formação superior", body="É a base: fisiologia, anatomia, biomecânica e metodologia do treinamento."),
  dict(k="point", n="02", title="Especialização no esporte", body="HYROX, CrossFit, fisiculturismo… cada modalidade tem exigências próprias."),
  dict(k="point", n="03", title="Vivência prática", body="Acompanhar atletas, ir a competições, aprender com quem já faz."),
  dict(k="point", n="04", title="Avaliação e dados", body="Medir, testar e ajustar. Treinador de alto rendimento trabalha com números."),
  dict(k="point", n="05", title="Resultado documentado", body="O seu portfólio são os seus atletas. Registre a evolução de cada um."),
  dict(k="cta", title="Em qual passo você está?", body="Comenta o número. E segue o Radar."),
], caption="""Treinador de alto rendimento não nasce pronto. É construção.

1️⃣ Formação superior
2️⃣ Especialização no esporte
3️⃣ Vivência prática
4️⃣ Avaliação e dados
5️⃣ Resultado documentado

O primeiro passo é o que sustenta todos os outros. Hoje existe até graduação tecnológica focada em musculação e preparação de atletas, como o Tecnólogo em Musculação e Fisiculturismo.

Em qual passo você está? 👇

""" + TAGS_CARREIRA + " #treinador #altorendimento"),

# 15
dict(id="15", fmt="C", slides=[
  dict(k="cover", tag="FORMAÇÃO", title="Tecnólogo em Musculação e Fisiculturismo", sub="A graduação para quem vive de treino de força →"),
  dict(k="point", n="01", title="Graduação tecnológica", body="Curso superior registrado no e-MEC, ofertado pela CEBEES em parceria com a FAEP."),
  dict(k="point", n="02", title="Foco total", body="Musculação, hipertrofia, preparação de atletas e fisiculturismo. Sem enrolação."),
  dict(k="point", n="03", title="Para quem é", body="Quem quer trabalhar com treino de força e quer formação superior na área."),
  dict(k="point", n="04", title="Turma de lançamento", body="A primeira turma tem condição especial de lançamento."),
  dict(k="cta", title="Quer saber mais?", body="Link na bio. Ou comenta \"TMF\" que a gente te chama."),
], caption="""Para quem quer transformar treino de força em profissão: Tecnólogo em Musculação e Fisiculturismo (TMF).

✅ Graduação tecnológica registrada no e-MEC
✅ Ofertado pela CEBEES em parceria com a FAEP
✅ Foco em musculação, hipertrofia e preparação de atletas

A primeira turma tem condição especial de lançamento.

👉 Link na bio ou comenta "TMF" que a gente te chama.

""" + TAGS_CARREIRA + " #musculacao #fisiculturismo #CEBEES"),
]
