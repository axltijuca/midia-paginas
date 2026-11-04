# Conteúdo dos 15 posts do @labdahipertrofia
HANDLE = "@labdahipertrofia"

TAGS = "#hipertrofia #musculacao #fisiculturismo #bodybuilding #treinodeforca #tecnologoemeducacaofisica"
TAGS_CARREIRA = "#tecnologoemeducacaofisica #tecnologoemmusculacao #educacaofisica #musculacao #fisiculturismo #personaltrainer"
AVISO = "⚠️ Conteúdo educativo. Não é recomendação de uso. Qualquer substância deve ser avaliada por um médico."

POSTS = [
# 1
dict(id="01", fmt="C", slides=[
  dict(k="cover", tag="ERGOGÊNICOS", title="Recurso ergogênico: o que é (e não é só \"bomba\")", sub="Os 5 tipos →"),
  dict(k="point", n="01", title="Nutricionais", body="Tudo que vem da alimentação e da suplementação: creatina, cafeína, proteína, carboidrato no treino."),
  dict(k="point", n="02", title="Farmacológicos", body="Medicamentos e hormônios. A maioria é proibida no esporte e todos exigem acompanhamento médico."),
  dict(k="point", n="03", title="Fisiológicos", body="Estratégias que mexem na fisiologia: treino em altitude, aquecimento bem feito, manejo do sono."),
  dict(k="point", n="04", title="Psicológicos", body="Foco, visualização, música no treino. Parece pouco, mas a ciência mostra efeito real."),
  dict(k="point", n="05", title="Mecânicos", body="Equipamentos que melhoram o desempenho: cinto, joelheira, tênis de levantamento, munhequeira."),
  dict(k="cta", title="Qual você mais usa?", body="Comenta o número. E segue o Lab pra entender cada um com ciência."),
], caption="""Recurso ergogênico é qualquer coisa que melhora o desempenho. Não é sinônimo de esteroide.

Café antes do treino? Ergogênico. Cinto no agachamento? Ergogênico. Música alta? Também.

Entender os tipos é o primeiro passo pra separar o que funciona, o que é marketing e o que é risco. É exatamente isso que vamos fazer aqui no Lab.

Qual desses você mais usa? 👇

""" + TAGS + " #ergogenicos #suplementacao"),

# 2
dict(id="02", fmt="C", slides=[
  dict(k="cover", tag="SUPLEMENTOS", title="Creatina: o que a ciência já confirmou", sub="Sem achismo →"),
  dict(k="point", n="01", title="Funciona", body="É um dos suplementos mais estudados do mundo. Aumenta força e ganho de massa magra quando somada ao treino."),
  dict(k="point", n="02", title="Monohidratada basta", body="As versões \"premium\" não mostraram vantagem consistente sobre a creatina monohidratada."),
  dict(k="point", n="03", title="Saturação é opcional", body="Tomar todo dia satura os músculos em algumas semanas. A fase de saturação só acelera esse processo."),
  dict(k="point", n="04", title="E o rim?", body="Em pessoas saudáveis, os estudos não mostram dano renal. Mas ela eleva a creatinina do exame — avise seu médico."),
  dict(k="cta", title="Você toma creatina?", body="Conta aí. E salva pra mandar pra quem ainda tem medo."),
], caption="""Creatina é o suplemento com mais evidência científica para quem treina. Ponto.

✅ Aumenta força e massa magra
✅ A monohidratada comum já resolve
✅ Não precisa de saturação (mas acelera)
⚠️ Ela eleva a creatinina no exame de sangue — isso não é lesão renal, mas o médico precisa saber

Quem tem doença renal ou qualquer condição de saúde deve conversar com o médico antes.

Salva e manda pra quem acha que creatina é "bomba" 👇

""" + TAGS + " #creatina #suplementacao"),

# 3
dict(id="03", fmt="P", slides=[
  dict(k="news", tag="DOPING", kicker="ENHANCED GAMES · LAS VEGAS", title="Os \"Jogos com doping liberado\" prometeram recordes. Saiu só um.", body="E atletas que declararam competir limpos venceram provas."),
], caption="""Em maio, Las Vegas recebeu o Enhanced Games: uma competição em que o uso de substâncias proibidas era permitido.

A promessa era uma chuva de recordes mundiais. Na prática, só um foi superado (50 m livre, com Kristian Gkolomeev) — e nem conta oficialmente, porque o evento está fora do sistema antidoping.

O detalhe mais curioso: algumas provas foram vencidas por atletas que declararam competir sem drogas.

A lição pra quem treina: substância nenhuma substitui treino, genética e anos de consistência. E o risco à saúde continua existindo.

O que você acha desse tipo de evento? 👇

""" + TAGS + " #doping #enhancedgames"),

# 4
dict(id="04", fmt="C", slides=[
  dict(k="cover", tag="SUPLEMENTOS", title="Cafeína: quando ajuda e quando atrapalha", sub="Arrasta →"),
  dict(k="point", n="01", title="Ajuda", body="Melhora força, resistência e foco. É um dos ergogênicos com evidência mais sólida."),
  dict(k="point", n="02", title="Timing", body="O efeito aparece em cerca de 30 a 60 minutos. Por isso o café vai antes do treino, não durante."),
  dict(k="point", n="03", title="Atrapalha o sono", body="Treina à noite? A cafeína pode ficar horas no organismo. Sono ruim derruba a hipertrofia."),
  dict(k="point", n="04", title="Mais não é melhor", body="Excesso causa ansiedade, taquicardia e tremor. Quem tem problema cardíaco ou de pressão deve falar com o médico."),
  dict(k="cta", title="Pré-treino ou café?", body="Comenta qual é o seu."),
], caption="""Cafeína é o pré-treino mais antigo (e mais estudado) que existe.

Funciona pra força, resistência e foco. Mas tem dois lados:
☕ Se você treina à noite, pode estar trocando desempenho por sono ruim
☕ Excesso dá ansiedade, taquicardia e tremedeira

O equilíbrio está na dose, no horário e na sua tolerância. Quem tem problema cardíaco ou de pressão deve conversar com o médico antes.

Pré-treino ou café? 👇

""" + TAGS + " #cafeina #pretreino"),

# 5
dict(id="05", fmt="C", slides=[
  dict(k="cover", tag="SAÚDE", title="Esteroides: os efeitos colaterais que ninguém posta", sub="Leia até o fim →"),
  dict(k="point", n="01", title="Coração", body="Queda do HDL (colesterol bom), aumento da pressão e alterações no músculo cardíaco."),
  dict(k="point", n="02", title="Hormônios", body="O corpo reduz ou para a produção natural de testosterona. Pode causar infertilidade."),
  dict(k="point", n="03", title="Fígado", body="Algumas substâncias orais são tóxicas para o fígado."),
  dict(k="point", n="04", title="Pele, cabelo e mama", body="Acne, queda de cabelo e ginecomastia (crescimento de tecido mamário nos homens)."),
  dict(k="point", n="05", title="Cabeça", body="Irritabilidade, alterações de humor e, ao parar, risco de sintomas depressivos."),
  dict(k="point", n="!", title="O recado", body="Isso não é recomendação de uso. Se você usa ou pensa em usar, o primeiro passo é um médico e exames."),
], caption="""Ninguém posta o exame de sangue. Só o shape.

Esteroides anabolizantes têm efeitos colaterais sérios, que vão do coração à fertilidade. Muitos são silenciosos — você só descobre no exame ou quando o problema já apareceu.

Este perfil não incentiva o uso. Falamos do assunto porque ele existe, é comum nas academias e informação séria salva vidas.

Se você usa ou está pensando em usar, procure um médico e faça exames.

""" + AVISO + "\n\n" + TAGS + " #saude"),

# 6
dict(id="06", fmt="P", slides=[
  dict(k="myth", tag="MITO X VERDADE", mito="Whey engorda.", verdade="O que engorda é excesso de calorias no total do dia. Whey é só proteína em pó."),
], caption="""❌ Mito: whey engorda.
✅ Verdade: whey é proteína, como frango ou ovo, só que em pó. O que faz ganhar gordura é passar das calorias que você gasta no dia.

Qual mito você mais ouve na academia? Manda nos comentários que a gente responde nos próximos posts 👇

""" + TAGS + " #whey #mitosdaacademia"),

# 7
dict(id="07", fmt="C", slides=[
  dict(k="cover", tag="SAÚDE", title="Os exames que quem treina pesado deveria fazer", sub="Salva este →"),
  dict(k="list", title="O básico", items=["Hemograma completo","Colesterol e triglicerídeos","Glicemia e hemoglobina glicada","Função do fígado (TGO, TGP, GGT)","Função dos rins (creatinina, ureia)"]),
  dict(k="list", title="Hormônios", items=["Testosterona total e livre","Estradiol","LH e FSH","Prolactina","TSH (tireoide)"]),
  dict(k="point", n="!", title="Quem pede é o médico", body="A lista é um ponto de partida para a conversa, não um autodiagnóstico. Quem interpreta e decide é o médico."),
  dict(k="cta", title="Quando foi seu último exame?", body="Se passou de um ano, marca o médico. E salva este post."),
], caption="""Treinar pesado e nunca fazer exame é dirigir sem painel.

O básico já mostra muita coisa: hemograma, colesterol, glicemia, fígado e rins. Os hormônios completam o quadro, principalmente pra quem usa ou já usou alguma substância.

Lembrando: essa lista é ponto de partida pra conversar com o médico. Quem pede, interpreta e conduz é ele.

Quando foi seu último exame? 👇

""" + TAGS + " #examesdesangue #saude"),

# 8
dict(id="08", fmt="C", slides=[
  dict(k="cover", tag="ANTIDOPING", title="Como funciona o antidoping (e por que existe o \"natural\" e o \"open\")", sub="Arrasta →"),
  dict(k="point", n="01", title="A lista proibida", body="A Agência Mundial Antidoping (WADA) publica todo ano a lista de substâncias e métodos proibidos."),
  dict(k="point", n="02", title="Em competição e fora dela", body="Atletas podem ser testados no dia da prova e também de surpresa, durante a temporada."),
  dict(k="point", n="03", title="Passaporte biológico", body="Em vez de procurar só a substância, monitora marcadores do sangue ao longo do tempo e detecta alterações."),
  dict(k="point", n="04", title="Natural x Open", body="No fisiculturismo, federações naturais fazem testes. Nas categorias open, muitas vezes o controle não existe."),
  dict(k="cta", title="Você competiria natural ou open?", body="Comenta. A gente quer saber."),
], caption="""Por que alguns atletas são pegos e outros não? Entender o antidoping ajuda a responder.

A WADA define o que é proibido. Os testes acontecem em competição e fora dela. E o passaporte biológico acompanha o atleta ao longo do tempo, não só no dia da prova.

No fisiculturismo, a realidade é diferente: existem federações naturais, com teste, e categorias open, onde muitas vezes não há controle.

Você competiria natural ou open? 👇

""" + TAGS + " #antidoping #natural"),

# 9
dict(id="09", fmt="C", slides=[
  dict(k="cover", tag="PEPTÍDEOS", title="Peptídeos: hype x evidência", sub="O que sabemos de verdade →"),
  dict(k="point", n="01", title="O que são", body="Cadeias curtas de aminoácidos. Alguns viraram medicamentos com muita evidência, como os análogos de GLP-1."),
  dict(k="point", n="02", title="O problema", body="Muitos peptídeos populares na academia têm estudos só em animais ou em laboratório. Faltam estudos em humanos."),
  dict(k="point", n="03", title="Mercado cinza", body="Sem regulação, não há garantia do que está no frasco: dose, pureza e contaminação."),
  dict(k="point", n="04", title="Conclusão", body="Promessa não é prova. Peptídeo é medicamento: só com prescrição e acompanhamento médico."),
  dict(k="cta", title="Quer mais sobre peptídeos?", body="Comenta qual você quer que a gente analise."),
], caption="""Peptídeos viraram moda nas academias. Mas qual é a diferença entre o que tem evidência e o que é só promessa?

Alguns, como os análogos de GLP-1, são medicamentos aprovados, com estudos robustos. Outros muito vendidos têm pesquisa apenas em animais — e circulam sem nenhuma regulação.

Antes de acreditar em qualquer "milagre", pergunte: tem estudo em humanos? Quem prescreve? De onde vem o produto?

Qual peptídeo você quer que a gente analise? 👇

""" + AVISO + "\n\n" + TAGS + " #peptideos"),

# 10
dict(id="10", fmt="P", slides=[
  dict(k="news", tag="OLYMPIA 2026", kicker="LAS VEGAS · SET/2026", title="Nick Walker é o Mr. Olympia 2026. E o Brasil levou dois títulos.", body="Natalia Coelho (Women's Physique) e Eduarda Bezerra (Wellness) são campeãs."),
], caption="""🏆 Olympia 2026 — Las Vegas.

👉 Men's Open: Nick Walker é o novo Mr. Olympia
🇧🇷 Women's Physique: Natalia Coelho, campeã
🇧🇷 Wellness: Eduarda Bezerra, campeã
🇧🇷 212: Lucas Garcia, vice-campeão

O Brasil segue como uma das maiores potências do fisiculturismo mundial. E isso movimenta toda a cadeia: atletas, treinadores e preparadores.

Quem foi seu destaque? 👇

""" + TAGS + " #mrolympia #olympia2026"),

# 11
dict(id="11", fmt="C", slides=[
  dict(k="cover", tag="TREINO", title="Volume x intensidade: o que mais importa para hipertrofia?", sub="Arrasta →"),
  dict(k="point", n="01", title="Volume", body="Número de séries difíceis por músculo na semana. Mais volume tende a gerar mais hipertrofia — até um limite."),
  dict(k="point", n="02", title="Intensidade", body="O quão perto da falha você chega. Séries longe da falha estimulam pouco."),
  dict(k="point", n="03", title="Os dois juntos", body="Volume com séries fáceis não funciona. Intensidade máxima sem volume também não. Precisa equilibrar."),
  dict(k="point", n="04", title="E a recuperação?", body="Volume e intensidade só viram músculo se você recupera. Sono e alimentação fecham a conta."),
  dict(k="cta", title="Quantas séries você faz por músculo?", body="Comenta. E segue o Lab."),
], caption="""Volume ou intensidade? A resposta da ciência: os dois — e a recuperação.

Séries demais longe da falha não estimulam. Séries até a falha demais não deixam recuperar. A hipertrofia acontece no equilíbrio.

Por isso montar treino é mais do que copiar planilha: exige entender as variáveis e ajustar para cada pessoa.

Quantas séries por músculo você faz na semana? 👇

""" + TAGS + " #volumedetreino"),

# 12
dict(id="12", fmt="C", slides=[
  dict(k="cover", tag="CARREIRA", title="Quem pode prescrever o treino de um fisiculturista?", sub="Arrasta →"),
  dict(k="point", n="01", title="Treino", body="No Brasil, prescrever exercício é atividade do profissional de Educação Física, pela Lei 9.696/98."),
  dict(k="point", n="02", title="Dieta", body="Plano alimentar é com nutricionista."),
  dict(k="point", n="03", title="Medicamentos", body="Qualquer substância ou hormônio é com médico. Ponto."),
  dict(k="point", n="04", title="A equipe", body="Atleta de alto nível tem treinador, nutricionista e médico trabalhando juntos."),
  dict(k="point", n="→", title="E a formação?", body="Bacharelado, tecnólogo ou pós: quem estuda musculação a fundo se destaca na preparação de atletas."),
  dict(k="cta", title="Você trabalha com atletas?", body="Comenta. No próximo post: o que estudar."),
], caption="""Preparar um fisiculturista é trabalho de equipe.

🏋️ Treino: profissional de Educação Física
🥗 Dieta: nutricionista
💊 Qualquer substância: médico

Cada um no seu papel. E para quem quer ser o treinador nessa equipe, formação específica faz toda a diferença — seja bacharelado, tecnólogo ou pós-graduação na área.

Você trabalha ou quer trabalhar com atletas? 👇

""" + TAGS_CARREIRA + " #treinador"),

# 13
dict(id="13", fmt="P", slides=[
  dict(k="poll", tag="ENQUETE", title="Se fosse competir no fisiculturismo, você iria:", a="NATURAL", b="OPEN"),
], caption="""Só pode escolher um 👇

🅰️ Natural (com teste antidoping)
🅱️ Open

Comenta A ou B e conta por quê.

""" + TAGS + " #natural"),

# 14
dict(id="14", fmt="C", slides=[
  dict(k="cover", tag="CARREIRA", title="O que um especialista em musculação precisa dominar", sub="A lista completa →"),
  dict(k="list", title="A base", items=["Fisiologia do exercício","Anatomia e cinesiologia","Biomecânica dos exercícios","Avaliação física"]),
  dict(k="list", title="A especialização", items=["Periodização para hipertrofia e força","Preparação de atletas","Recursos ergogênicos e antidoping","Nutrição aplicada ao treino"]),
  dict(k="point", n="→", title="Onde aprender", body="Existe graduação focada nisso: o Tecnólogo em Musculação e Fisiculturismo."),
  dict(k="cta", title="O que falta pra você?", body="Comenta qual desses temas você mais quer estudar."),
], caption="""Ser bom em musculação não é só treinar pesado. É dominar a ciência por trás do treino.

Fisiologia, biomecânica, periodização, avaliação, ergogênicos e antidoping. Tudo isso separa o profissional que entrega resultado do que só repete o que viu na internet.

E hoje já existe formação superior inteira focada nisso: o Tecnólogo em Musculação e Fisiculturismo. Vamos falar dele no próximo post.

Qual desses temas você mais quer estudar? 👇

""" + TAGS_CARREIRA),

# 15
dict(id="15", fmt="C", slides=[
  dict(k="cover", tag="FORMAÇÃO", title="Tecnólogo em Musculação e Fisiculturismo", sub="Ciência do treino virando profissão →"),
  dict(k="point", n="01", title="Graduação tecnológica", body="Curso superior registrado no e-MEC, ofertado pela CEBEES em parceria com a FAEP."),
  dict(k="point", n="02", title="Foco total", body="Hipertrofia, força, preparação de atletas e fisiculturismo, do básico ao alto rendimento."),
  dict(k="point", n="03", title="Para quem é", body="Quem vive musculação e quer transformar isso em formação superior e carreira."),
  dict(k="point", n="04", title="Turma de lançamento", body="A primeira turma tem condição especial."),
  dict(k="cta", title="Quer saber mais?", body="Link na bio. Ou comenta \"TMF\" que a gente te chama."),
], caption="""Você já estuda treino por conta própria. Que tal transformar isso em graduação?

Tecnólogo em Musculação e Fisiculturismo (TMF):
✅ Graduação tecnológica registrada no e-MEC
✅ Ofertado pela CEBEES em parceria com a FAEP
✅ Foco em hipertrofia, força e preparação de atletas

A primeira turma tem condição especial de lançamento.

👉 Link na bio ou comenta "TMF" que a gente te chama.

""" + TAGS_CARREIRA + " #CEBEES"),
]
