import os
import time
import sys

def limpar():
    os.system('cls')

def dig(texto, pausa=1):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.05)
    print()
    time.sleep(pausa)

def cena_rua():
    dig(f'{nome} pega o rumo de casa e se depara com uma rua movimentada, mas tem uma faixa de pedestre, o que ele faz?')
    
    print("""
1 - Atravessa correndo, arriscando-se entre os carros.
2 - Espera o sinal abrir para os pedestres.
3 - Desiste da avenida e tenta pegar um caminho alternativo.
    """)
    
    opc1_1 = input("Escolha sua ação (1,2,3): ")
    limpar()
    
    if opc1_1 == '1':
        print(''' 
                    /\\      _____          _____  
     ,-----,       /  \\____/__|__\_    ___/__|__\___ 
  ,--'---:---`--, /  |  _     |     `| |      |      `|
 ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'    
``````````````````````````````````````````````````````````````''')
        dig(f"{nome} respira fundo, corre pela faixa e quase é atingido por um carro!")
        dig("Por sorte, o motorista freia a tempo, mas ele escuta uma buzina e xingamentos ecoando.")
        dig("Com o coração acelerado, ele chega do outro lado da rua.")
        dig('depois de atravessar a rua ele anda um pouco e vê a mercearia...')
        limpar()
        cena_mercado()
        
    elif opc1_1 == '2':
        print('''
        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        |  ___  |
         \_____/
      ____|  |____
     /    \__/    \
    /              \
   /\_/|        |\_/\
  / /  |        |  \ \
 ( <   |        |   > )
  \ \  |        |  / /
   \ \ |________| / /''')
        dig(f"{nome} espera pacientemente. O sinal finalmente abre para os pedestres.")
        dig("Ele atravessa com calma, observando a cidade agitada ao seu redor.")
        dig('depois de atravessar a rua ele anda um pouco e vê a mercearia...')
        limpar()
        cena_mercado()
        
    elif opc1_1 == '3':
        dig(f"{nome} decide não arriscar e vira à esquerda, procurando outro caminho.")
        dig("Decidido a ir no centro ele senta na praça e vê o movimento")
        dig('Depois de ficar um tempo na praça decide ir a mercearia comprar algo...')
        limpar()
        cena_mercado()
limpar()
        
        
def cena_mercado():

    dig(f"A curiosidade fala mais alto. {nome} entra na mercearia iluminada por lâmpadas fracas.")
    dig("O ambiente tem cheiro de café recém-passado, e o dono, um senhor simpático, o cumprimenta.")
    
    print("""
    1 - Compra algo rápido para comer no caminho.
    2 - Decide puxar conversa com o dono do mercado.
    3 - Repara em uma prateleira bagunçada e se aproxima curioso.
    """)
    
    opc1_2 = input("Escolha sua ação (1,2,3): ")
    limpar()
    
    if opc1_2 == '1':
        dig(f"{nome} pega um salgadinho e uma garrafinha de água, paga rapidamente e volta para a rua.")
        dig("O lanche pode ser útil mais tarde...")
        dig(f'depois de comprar o lanche, {nome} decide sair novamente para rua, onde o senhor ainda estava a sua espreita, olhando fixamente para ele...')
        limpar()
        cena_velho()
        
    elif opc1_2 == '2':
        dig("Ele se aproxima do balcão e começa a conversar com o dono.")
        dig(f"O senhor comenta que aquela noite parecia estranhamente agitada, e aconselha {nome} a ter cuidado.")
        dig('diz que na cidade parece estar tendo uma espécie de seita maligna')
        dig('e que estao capturando pessoas a noite sem motivo...')
        limpar()
        dig(f'{nome} encara isso como algo assustador! e se despede do dono indo a caminho da saida.')
        dig('olhando discretamente pra tras ele encontra um livro jogado em meio as prateleiras, e pega rapidamente o livro com a capa chamativa...')
        dig('desncendo a escada da mercearia ele vai rumo a rua.')
        dig('olhando pra rua ele vê novamente o velho olhando para ele com um sorriso pertubador sem motivo...')
        limpar()
        cena_velho()
        
    elif opc1_2 == '3':
        dig(f"Ao se aproximar da prateleira, {nome} percebe um pequeno caderno esquecido entre os produtos.")
        dig("Será apenas um erro de organização ou algo mais importante?")
        limpar()
        dig(f'{nome} pega o caderno, esconde entre suas roupas e se despede do dono da mercearia rapidamente.')
        dig('saindo da mercearia othavyo trava por alguns segundos, estava la! o velho!')
        dig(f'{nome} olha para ambos os lados e nao tinha ninguem além daquele homem a sua frente...')
        limpar()
        cena_velho()
limpar()


def cena_velho():
    dig(f"{nome} respira fundo e decide se aproximar do homem parado na calçada.")
    dig("O estranho parece cansado, mas seus olhos brilham como se estivesse esperando exatamente por ele.")
    limpar()
    
    print("""
    1 - Cumprimenta o homem educadamente.
    2 - Pergunta diretamente o que ele está olhando.
    3 - Ignora o silêncio e segue andando, fingindo que não viu nada.
    """)
    
    opc1_3 = input("Escolha sua ação (1,2,3): ")
    limpar()

    if opc1_3 == '1':
        dig("O homem sorri discretamente e responde com a voz baixa: 'Boa noite, garoto... cuidado com quem cruza seu caminho hoje, ahh, quase me esqueci, cuidado com esse caderno que você pegou... nele contem coisas que não são do entendimento da grande massa...'")
        dig('o homem se esvai na escuridao e neblina da rua com um sorriso...')
        limpar()
        dig('eu me pergunto como esse velho me viu pegando o livro... fui bastante discreto quanto a isso.')
        dig(f'{nome} vai pra casa meio confuso e bastante curioso sobre esse livro.')
        limpar()
        cena_caderno()
                
    elif opc1_3 == '2':
        dig(f"{nome} encara o homem e pergunta o motivo daquele olhar fixo.")
        dig("O estranho apenas dá uma risada curta e diz: 'Logo você entenderá... este livro que você possui irá te mostrar coisas que não gostaria que ficasse em sua memória.'")
        limpar()
        dig(f'**{nome} fica sem reação ao perceber que aquele velho o viu pegando o livro na mercearia...')
        limpar()
        dig('como você me viu pegando o livro? e o que você tem a ver com isso?')
        dig('** o velho simplesmente vai embora cantarolando uma musica arrepiante sem te dar ouvidos...')
        dig(f'{nome} volta pra casa meio assustado e confuso, mas isso só instiga sua curiosidade!')
        limpar()
        cena_caderno()
        
    elif opc1_3 == '3':
        dig(f"{nome} acelera o passo e finge que não viu nada.")
        dig("Mesmo assim, ele sente os olhos do homem o seguindo até virar a esquina...")
        limpar()
        dig(f'**ao virar a esquina para ir para casa o velho esta logo a frente dele, {nome} se assuta ao ver aquele mesmo homem a sua frente parado.')
        dig(f'** {nome} chega até o homem com um pouco de medo e pergunta o que ele quer...')
        limpar()
        dig('** o velho se aproxima e diz: Garoto cuidado com este livro que você possui, depois de uma vez aberto você nunca mais será o mesmo...')
        dig(f'**{nome} olha meio confuso, pensa, (COMO ESSE VELHO SABE QUE PEGUEI O LIVRO NA MERCEARIA???)')
        dig('**incrédulo com a situação ele se faz de bobo e toma o rumo de casa apressado...')
        limpar()
        cena_caderno()
limpar()

def cena_caderno():
    print('''
               )
         ( _   _._
          |_|-'_~_`-._
       _.-'-_~_-~_-~-_`-._
   _.-'_~-_~-_-~-_~_~-_~-_`-._
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |  []  []   []   []  [] |
    |           __    ___   |
  ._|  []  []  | .|  [___]  |_._._._._._._._._._._._._._._._._.
  |=|________()|__|()_______|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|
^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    _______      ===
   <_#####_>       ===
      ^|^             ===
       |                 ===      
          ''')
    dig(f"{nome} chega em casa, fecha a porta devagar e senta à mesa com o caderno misterioso.")
    dig("Ele abre o livro e começa a folhear as páginas, repletas de símbolos estranhos e anotações perturbadoras.")
    dig("Enquanto lê, algumas palavras parecem saltar da página, quase sussurrando para ele...")
    limpar()
    
    print("""
1 - Ignorar os barulhos e continuar lendo atentamente.
2 - Levantar-se e tentar ouvir de onde vêm os sons.
3 - Fechar o livro e investigar a casa com cuidado.
""")
    
    opc_caderno = input("Escolha sua ação (1,2,3): ")
    limpar()
    
    if opc_caderno == '1':
        dig(f"{nome} decide focar apenas no livro, anotando símbolos e frases sobre uma tal seita do 'Sol Negro'.")
        dig("Ele percebe que quanto mais lê, mais estranhos os barulhos em casa se tornam: passos, sussurros, portas rangendo...")
        dig("O coração acelera, mas ele sente que precisa continuar estudando o conteúdo do caderno.")
        limpar()
        dig(f'{nome} verifica no notebook se exite algo sobre esse nome, procura imagens, arquivos historicos, mas nao encontra nada!')
        dig("Enquanto isso, percebe um padrão nas anotações que indica que a seita está observando pessoas na cidade.")
        dig(f"Decidido, {nome} anota tudo e prepara-se para investigar mais profundamente na próxima noite.")
        limpar()
        cena_noite()
    
    elif opc_caderno == '2':
        dig(f"{nome} se levanta e caminha cautelosamente pela casa, tentando localizar a origem dos barulhos.")
        dig("Ao entrar na cozinha, uma sombra passa rapidamente, e uma voz baixa sussurra: 'O que você fez...?'")
        dig("Assustado, ele volta à mesa e encara o caderno. As anotações de uma tal seita do 'Sol Negro' parecem mais reais e perigosas do que nunca.")
        limpar()
        dig("Com medo, mas curioso, ele decide continuar estudando, sabendo que cada página lida o aproxima de algo desconhecido.")
        dig(f'{nome} fica decidido de na proxima noite investigar com cautela tudo isso, pois nunca viu algo parecido na cidade.')
        limpar()
        cena_noite()
    
    elif opc_caderno == '3':
        dig(f"{nome} fecha o caderno, mas algo dentro da casa parece se mover sozinho. Objetos tilintam e passos ecoam pelos corredores.")
        dig("Ele investiga cada cômodo com cuidado, mas não vê ninguém. A sensação de estar sendo observado aumenta a cada instante.")
        dig("Voltando à mesa, ele abre o caderno novamente, percebendo símbolos que antes não tinha notado. A seita do 'Sol Negro' parece ter planos mais próximos do que imaginava.")
        limpar()
        dig(f"Ao final da noite, {nome} decide que precisa se preparar melhor para entender tudo sobre o caderno e a seita.")
        dig("Ele organiza anotações, faz pesquisas e se prepara para a próxima fase de investigação.")
        dig("Algo indica que amanhã ele terá que sair novamente para descobrir mais...")
        dig(f'{nome} fica decidido de investigar isso na proxima noite!')
        limpar()
        cena_noite()
limpar()
    
def cena_noite():
    dig(f"A noite cai e {nome} sente que algo estranho ainda paira sobre a cidade.")
    dig("Ele resolve sair de casa para investigar pistas sobre a seita do 'Sol Negro', seguindo anotações do caderno.")
    dig("As ruas estão silenciosas, mas sombras se movem entre os prédios, e sussurros surgem do nada...")

    print("""
1 - Seguir andando pela cidade e olhar os lugares atentamente...
2 - Entrar por becos escuros, buscando lugares que o caderno indicou.
3 - Voltar para casa e tentar pesquisar mais calmamente, evitando sair à noite.
""")
    
    opc_noite = input("Escolha sua ação (1,2,3): ")
    limpar()
    
    if opc_noite == '1':
        dig(f"{nome} caminha por um bairro mais afastado do centro, e acha alguns prédios abandonados...")
        dig("Ele vê umas pessoas encapuzadas andando e fazendo grunidos entre os prédios.")
        limpar()
        dig("olhando aquela janela que parecia ser no quinto andar com uma luz fraca (provavelmente velas) ele suspeita que algo de ruim esta acontecendo ali.")
        dig("Ele decide ir até o prédio abandonado ouvir e tentar capturar provas de algo para levar a polícia.")
        dig('passando pelas ruas para voltar pra casa ele se depara com alguns becos...')
        limpar()
        dig(f"{nome} se aventura pelos becos escuros, seguindo as pistas do caderno.")
        dig("Ele procura algo que possa servir como prova da seita do 'Sol Negro'.")
        dig("Entre sombras e paredes sujas, encontra velas derretidas espalhadas pelo chão e manchas de sangue em algumas partes.")
        limpar()
        dig("Ele fotografa discretamente tudo, tentando registrar cada detalhe sem ser visto.")
        dig("Enquanto examina o local, ouve chutes abafados vindo da parede da casa escura ao lado, como se alguém estivesse pedindo ajuda por dentro de algum porão...")
        limpar()
        cena_noite_final()
    
    elif opc_noite == '2':
        dig(f"{nome} se aventura pelos becos escuros, seguindo as pistas do caderno.")
        dig("Ele procura algo que possa servir como prova da seita do 'Sol Negro'.")
        dig("Entre sombras e paredes sujas, encontra velas derretidas espalhadas pelo chão e manchas de sangue em algumas partes.")
        limpar()
        dig("Ele fotografa discretamente tudo, tentando registrar cada detalhe sem ser visto.")
        dig("Enquanto examina o local, ouve chutes abafados vindo da parede da casa escura ao lado, como se alguém estivesse pedindo ajuda por dentro de algum porão...")
        limpar()
        cena_noite_final()
    
    elif opc_noite == '3':
        dig(f"{nome} decide voltar para casa, para averiguar melhor o livro.")
        dig("Ele pesquisa mais sobre a seita do 'Sol Negro', mas cada página lida aumenta seu medo.")
        dig("Vozes sussurram pelos cantos da casa, e sombras parecem se mover com vontade própria.")
        limpar()
        dig("Mesmo dentro de casa, ele percebe que o caderno o trouxe para algo maior do que imaginava...")
        dig('com essas atormentações ele decidi ir pra rua refrescar a cabeça...')
        limpar()
        dig(f"{nome} se aventura pelos becos escuros, seguindo as pistas do caderno.")
        dig("Ele procura algo que possa servir como prova da seita do 'Sol Negro'.")
        dig("Entre sombras e paredes sujas, encontra velas derretidas espalhadas pelo chão e manchas de sangue em algumas partes.")
        limpar()
        dig("Ele fotografa discretamente tudo, tentando registrar cada detalhe sem ser visto.")
        dig("Enquanto examina o local, ouve chutes abafados vindo da parede da casa escura ao lado, como se alguém estivesse pedindo ajuda por dentro de algum porão...")
        limpar()
        cena_noite_final()
limpar()

def cena_noite_final():
    dig(f"{nome} respira fundo e decide entrar na casa escura, seguindo os passos abafados que ouviu anteriormente.")
    dig("A cada cômodo que passa, a tensão aumenta, e o silêncio é quebrado apenas pelo rangido do assoalho.")
    dig("Ele percebe uma escada que leva ao porão e sente que algo ou alguém está lá embaixo, provavelmente a garota que precisa ser resgatada.")
    
    print("""
1 - Desce silenciosamente a escada, tentando não fazer barulho.
2 - Entra correndo, sem pensar duas vezes, pronto para qualquer coisa.
3 - Dá uma volta pela casa primeiro, procurando outra entrada para o porão.
""")
    
    opc_final = input("Escolha sua ação (1,2,3): ")
    limpar()
    
    if opc_final == '1':
        dig(f"{nome} desce cuidadosamente a escada, atento a cada sombra.")
        dig("Ele encontra a garota acorrentada, assustada, e sussurra para ela se acalmar.")
        dig("Com esforço, consegue libertá-la, e juntos começam a subir de volta.")
        dig("Quando finalmente alcançam a saída, a garota, em um movimento inesperado, o atinge com uma garrafa na cabeça!")
        dig(f"{nome} cai desacordado.")
        
    elif opc_final == '2':
        dig(f"{nome} corre escada abaixo, pronto para confrontar qualquer ameaça.")
        dig("Encontra a garota, assustada e amarrada, e tenta libertá-la rapidamente.")
        dig("No instante em que saem do porão, a garota lhe dá uma garrafada na cabeça!")
        dig("Ele cai no chão, desmaiado.")
        
    elif opc_final == '3':
        dig(f"{nome} caminha pela casa procurando outra entrada, mas percebe que o tempo está contra ele.")
        dig("Decide voltar para a escada e desce rapidamente.")
        dig("Encontra a garota e a ajuda a escapar, mas antes que possam sair, ela o acerta com uma garrafa na cabeça.")
        dig("Ele desmaia instantaneamente.")
    
    limpar()
    
    dig(f"{nome} acorda assustado, amarrado em cima de uma mesa de sacrifício.")
    dig("Ao redor dele, pessoas encapuzadas formam um círculo, e a garota que ele acreditava ter salvado está na frente, sorrindo macabramente.")
    dig("Tudo não passou de uma armadilha para capturá-lo, e ele percebe que não há escapatória.")
    dig("Em meio ao horror e à confusão, tenta se debater para sair daquele lugar...")
    dig(f'nada adianta, parece que a vida de {nome} esta para acabar ali mesmo.')
    dig(f'a garota chega ao lado de {nome} e sussurra: você estava predestinado a isso!')
    dig("e tudo acaba ali..........")
    limpar()
    print('tnzr srvgb rz clguba cbe bgunilb')
    limpar()
    print('zryube uvfgbevn dhr pevrv ngé ubwr')
    limpar()
limpar()


print('''
                                                 
                                                 
 ░████████  ░██████   ░█████████████   ░███████  
░██    ░██       ░██  ░██   ░██   ░██ ░██    ░██ 
░██    ░██  ░███████  ░██   ░██   ░██ ░█████████ 
░██   ░███ ░██   ░██  ░██   ░██   ░██ ░██        
 ░█████░██  ░█████░██ ░██   ░██   ░██  ░███████  
       ░██                                       
 ░███████                                        
                                                                                                
\n\n''')

input('pressione enter...')
limpar()

nome = input('digite seu nome para começar o game: ')
limpar()

print('''
               __________                                 
             .'----------`.                              
             | .--------. |                             
             | |########| |       __________              
             | |########| |      /__________\             
    .--------| `--------' |------|    --=-- |-------------.
    |        `----,-.-----'      |o ======  |             | 
    |       ______|_|_______     |__________|             | 
    |      /  %%%%%%%%%%%%  \                             | 
    |     /  %%%%%%%%%%%%%%  \                            | 
    |     ^^^^^^^^^^^^^^^^^^^^                            | 
    +-----------------------------------------------------+
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
    ''')

dig('caramba, ja deu 17:00!')
dig('hora de ir embora...')
limpar()

dig(f'**{nome} junta suas coisas, desliga seu PC e se dispede da turma!**')

print('''
       xxxxxxxxxxxxxxxxxxxxxx
     xxxxxxxxxxxxxxxxxxxxxxxxxx    
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 XXXXXXXXXXXXXXXXXX         XXXXXXXX
XXXXXXXXXXXXXXXX              XXXXXXX
XXXXXXXXXXXXX                   XXXXX
 XXX     _________ _________     XXX   
  XX    I  _xxxxx I xxxxx_  I    XX       
 ( X----I         I         I----X )         
( +I    I         I         I    I+ )
 ( I    I         I         I    I )
  (I    I______ /   \_______I    I)
   I           ( ___ )           I
   I    _                   _    i
    \    \___           ___/    /
     \_      \_________/      _/
       \        \___,        /
         \                 /
          |\             /|
          |  \_________/  |''')

dig('\nflw turma até amanhã!')
limpar()

dig(f'{nome} sai pela porta da frente do seu trabalho e vê dois caminhos para seguir:\n')

dig('À direita, a rua que leva até sua casa.')
dig('À esquerda, uma pequena mercearia ainda aberta, apesar do horário.')
dig('Enquanto pensa no caminho, ele percebe um senhor parado perto da calçada, olhando fixamente para ele.')

print("""
O que você faz?
1 - segue direto pra casa
2 - decide entrar no mercado
""")

opc1 = input('digite uma das opções (1 ou 2): ')
limpar()   

if opc1 == '1':
    cena_rua()
elif opc1 == '2':
    cena_mercado()
    
final = dig(f'e esse é o final do game... {nome} teve um fim trágico!')
