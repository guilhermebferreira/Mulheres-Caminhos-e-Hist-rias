# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define personagem = Character("Personagem", who_color='#8904B1')
define marido = Character("Marido", who_color='#444444')
define chefe1 = Character("Chefe", who_color='#444444')
default karma = 0


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    jump rota_probelma_trabalho

    scene bg bairro

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.


    "Depois de um dia muito cansativo no trabalho"

    "Tudo que você quer é chegar em casa"

    "Mas ainda você ainda tem uma aula pra assitir..."

    personagem "Estou exausta."

    extend "\nAcho que não faria mal deixar de ir na pós só por hoje"

    menu:
        personagem "Então, será que..."

        "Vou direto pra casa, descançar um pouco seria bom":
            jump volta_pra_casa

        "Melhor ir pra faculdade":
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


    "Você esta ao mesmo tempo cansada pelo dia longo. \nE feliz por estar chegando em casa"

    "Você mora em um bairro afastado no entorno de brasília..."

    "Levando um dia após o outro..."

    "você tira a chave da bolsa e apenas de saber que esta chegando em casa..."

    extend "\nse sente leve"

    personagem "É sempre bom chegar em casa!"

    jump briga_com_marido_leve



label briga_com_marido_leve:
    scene bg sala 


    marido "Chegando tarde de novo?"

    show marido neutro at left:
        yalign 0.2
    marido "Já são quase nove, estou morrendo de fome"

    show marido neutro at left:
        yalign 0.2

    menu:

        "teste"

        "Tambem estou morrendo de fome, você chegou mais cedo? Poderia ter adiantado algo":
            $ karma -= 5
            jump vou_preparar_algo

        "Não tem como chegar mais cedo com essa rotina. Mas vou preparar algo gostoso pra gente":
            $ karma = 5
            jump vou_preparar_algo

        "Melhor eu ir direto pra cozinha preparar algo":
            $ karma -= 15
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
            $ karma -= 5
            jump dia2

        "...":

            $ karma += 5
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

    show chefe1 neutro:
        yalign 0.2

    chefe1 "Mocinha"

    extend "preciso que você cuide desses relatórios de balanço..."

    menu:
        personagem "(\"mocinha\", Odeio que me chamem assim)"

        "Pois não, como posso ajudar":
            personagem "Relatórios de balanço?"

        "Desculpa, esta falando comigo?":
            personagem "Relatórios de balanço?"

    personagem "Mas isso é responsabilidade de outro departamento..."

    chefe1 "Eles estão um pouco sobrecarregados esse semana"

    chefe1 "E alguem realmente precisa cuidar desses relatórios"

    show chefe1 satisfeito:
        yalign 0.2
    

    menu:
        chefe1 "Consegue me entregar ainda hoje?"

        "E quem me ajuda com a minhas demandas??":
            personagem "Relatórios de balanço?"

        "Tudo bem":
            personagem "Você não pediria se não fossem muito importantes, certo?"
            chefe1 "São bem mais do que isso mocinha"

    scene bg noite
    with fade

    hide chefe1

    "Você acaba ficando bem além do horario de expdiente para conseguir entregar todas as demanas"

    "Bem além do que pretendia"

    jump briga_com_marido_seria


label briga_com_marido_seria:

    scene bg sala
    with fade

    show marido zangado:
        yalign 0.2

    marido "Assim fica dificil"

    marido "Outro dia do mesmo jeito?"


    show marido gritando:
        yalign 0.2

    marido "Parece que você não tem consideração comigo"


    show marido neutro

    marido "Você não vai falar nada?"

    menu:

        "Mesmo exausta, seu marido te cobra que ainda faça cumpra com as obrigações da casa"

        "Você abaixa a cabeça e apenas consente.":
            $ karma -= 5
            jump rota_passiva

        "Você responde ao desaforo":

            $ karma += 5
            jump rota_atitude

    return

    
    
