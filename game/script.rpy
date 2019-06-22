# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define personagem = Character("Você", who_color='#8904B1')
define marido = Character("Marido", who_color='#444444')
define chefe1 = Character("Chefe", who_color='#222222')


default karma_autoestima = 0
default karma_estudo = 0

default karma_relacionamento = 0


# The game starts here.

label start:


    #jump final_na_empresa

    scene bg bairro



    "Depois de um dia muito cansativo no trabalho"

    show mulher_trabalho neutra:
        yalign 0.2

    "Tudo que você quer é chegar em casa"

    show mulher_trabalho triste:
        yalign 0.2

    "Mas ainda você ainda tem uma aula pra assistir..."

    personagem "Estou exausta."

    extend "\nAcho que não faria mal deixar de ir na pós só por hoje"

    menu:
        personagem "Então, será que..."

        "Vou direto pra casa, descançar um pouco seria bom":

            $ karma_estudo -= 10
            jump volta_pra_casa

        "Melhor ir pra faculdade":
            $ karma_estudo += 10
            jump vai_pra_faculdade





label vou_pra_cozinha:
    scene bg cozinha
    with fade


    show marido neutro:
        yalign 0.2

    personagem "você tem razão..."


    show marido satisfeito:
        yalign 0.2

    personagem "vou preparar alguma coisa pra gente comer"

    "..."
    jump outro_dia

label responde_desaforo:
    scene bg casa
    with fade


    show marido neutro:
        yalign 0.2

    personagem "você não vê que fiquei o dia inteiro dando duro"
    personagem "trabalhando pra ajudar a colocar comido aqui dentro de casa, assim como você"
    personagem "e ainda estudando pra tentar um futuro melhor pra gente"

    show marido zangado
    personagem "você acha que sou obrigada?"


    show marido zangado at left:
        yalign 0.2

    "..."
    jump outro_dia
 

 

label volta_pra_casa:
    scene bg onibus
    with fade

    "Em um dia comum, 40 minutos são suficentes para chegar em casa"

    "Mas um engarrafento em uma das vias principais te fez passar mais de 2 horas no onibus"


    jump chega_em_casa

label vai_pra_faculdade:
    scene bg aula
    with fade
    "Apesar de não ser sua disciplina preferida"
    "Você assistiu uma aula inspiradora"
    "Que acendeu novamente aquela esperança de um futuro melhor para você"
    "Uma carreira"

    jump chega_em_casa

label chega_em_casa:
    scene bg bairro
    with fade

    show mulher_trabalho neutra at right:
        yalign 0.2


    "Você está ao mesmo tempo cansada pelo dia longo. \nE feliz por estar chegando em casa"

    "Você mora em um bairro afastado no entorno de brasília..."
 

    "você tira a chave da bolsa e apenas de saber que está chegando em casa..."


    show mulher_trabalho sorrindo at right:
        yalign 0.2

    extend "\nse sente leve"

    personagem "É sempre bom chegar em casa!"

    jump briga_com_marido_leve



label briga_com_marido_leve:
    scene bg sala 


    marido "Você chegou bem tarde hoje"

    show marido neutro at left:
        yalign 0.2


    marido "Isto está começando a virar uma rotina pelo visto"
 

    show marido zangado at left:
        yalign 0.2



    marido "Enfim..."

    show marido neutro at left:
        yalign 0.2

    menu:

        
        marido "Já são quase nove, estou morrendo de fome"

        "Também estou morrendo de fome":


            show mulher_trabalho neutra at right:
                yalign 0.2

            personagem "Você chegou mais cedo..."
            personagem "Porque não preparou nada pra gente?"
            
            $ karma_relacionamento -= 10
            $ karma_autoestima += 10
            jump vou_preparar_algo

        "Não tem como chegar mais cedo com essa rotina. Mas vou preparar algo gostoso pra gente":
            
            

            show mulher_trabalho triste at right:
                yalign 0.2

            personagem "Estou estudando para conseguir um futuro melhor pra gente"



            show mulher_trabalho neutra at right:
                yalign 0.2
            personagem "Mas vou preparar algo gostoso para a gente comer"
            $ karma_relacionamento -= 10
            jump vou_preparar_algo

        "Melhor eu ir direto pra cozinha preparar algo":
            

            show mulher_trabalho triste at right:
                yalign 0.2


            personagem "Melhor eu ir direto pra cozinha preparar algo"

            $ karma_relacionamento += 10
            $ karma_autoestima -= 10
            jump vou_preparar_algo


label vou_preparar_algo:
    scene bg sala
    with fade


    show marido neutro:
        yalign 0.2

    marido "Você sabe que eu te amo"


    marido "Não sabe?"


    show marido satisfeito:
        yalign 0.2

    menu:

        "..."

        "Sim, eu sei":
            $ karma_relacionamento += 10
            jump dia2

        "...":
            $ karma_relacionamento -= 10
            jump dia2

    jump dia2


label dia2:
    scene bg noite
    with fade

    "Você foi dormir extausta esse dia"
 
    scene bg bairro
    with fade

    "No dia seguinte"

    extend ", você acordou bem cedo para não se atrasar para o trabalho"
    jump dia_cheio_trabalho

label dia_cheio_trabalho:
    scene bg trabalho1
    with fade

    personagem "Tenho tanta coisa pra fazer"

    personagem "Mal tenho conseguido dar conta dessas demandas..."

    show chefe1 neutro at left:
        yalign 0.2

    chefe1 "Mocinha"

    extend ", preciso que você cuide desses relatórios de balanço..."

    menu:
        personagem "(\"mocinha\", Odeio que me chamem assim)"

        "Pois não, como posso ajudar":
            show mulher_trabalho triste at right:
                yalign 0.2
            $ karma_autoestima -= 10
            chefe1 "Preciso desses relatórios de balanço para amanhã!"
            personagem "Relatórios de balanço?"

        "Desculpa, está falando comigo?":
            show mulher_trabalho neutra at right:
                yalign 0.2
            $ karma_autoestima += 10
            chefe1 "Preciso desses relatórios de balanço para amanhã!"
            personagem "Relatórios de balanço?"

    personagem "Mas isso é responsabilidade de outro departamento..."

    chefe1 "Eles estão um pouco sobrecarregados esse semana"

    chefe1 "E alguém realmente precisa cuidar desses relatórios"

    show chefe1 satisfeito:
        yalign 0.2
    

    menu:
        chefe1 "Consegue me entregar ainda hoje?"

        "E quem me ajuda com a minhas demandas??":
            personagem "E quem me ajuda com a minhas demandas?"

            $ karma_autoestima += 10

            jump relatorios

        "Tudo bem":
            personagem "Você não pediria se não fossem muito importantes, certo?"
            chefe1 "São bem mais do que isso mocinha"

            $ karma_autoestima -= 10
            jump relatorios

    jump relatorios


    


label relatorios:
    scene bg noite
    with fade
 

    "Você acaba ficando bem além do horario de expediente para conseguir entregar todas as demanas"

    "Bem além do que pretendia"

    jump briga_com_marido_seria


label briga_com_marido_seria:

    scene bg sala
    with fade

    show marido zangado at left:
        yalign 0.2

    marido "Assim fica dificil"

    marido "Outro dia do mesmo jeito?"


    show marido gritando at left:
        yalign 0.2

    marido "Parece que você não tem consideração comigo"


    show marido neutro at left:
        yalign 0.2

    marido "Você não vai falar nada?"

    show mulher_trabalho surpresa at right:
        yalign 0.2

    menu:

        "Mesmo exausta, seu marido te cobra que ainda faça cumpra com as obrigações da casa"

        "Você abaixa a cabeça e apenas consente.":
            
            show mulher_trabalho triste at right:
                yalign 0.2
            $ karma_relacionamento += 10
            jump rota_passiva

        "Você responde ao desaforo":
            show mulher_trabalho neutra at right:
                yalign 0.2
            $ karma_relacionamento = -10
            jump rota_atitude

    jump rota_passiva

    
    
