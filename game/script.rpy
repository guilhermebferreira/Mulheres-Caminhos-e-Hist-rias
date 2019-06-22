# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Personagem", who_color='#8904B1')
define m = Character("Marido", who_color='#444444')
default karma = 0


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bairro

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "Em um bairro afastado no entorno de brasília..."

    "No final do dia, após duas horas de ônibus"



    show voce cansada


    e"Você esta ao mesmo tempo cansada pelo dia longo. \nE feliz por estar chegando em casa"

    jump briga_com_marido_leve


label vou_pra_cozinha:
    scene bg cozinha
    with fade


    show marido neutro:
        yalign 0.2

    e "você tem razão..."


    show marido satisfeito:
        yalign 0.2

    e "vou preparar alguma coisa pra gente comer"

    "..."
    jump outro_dia

label responde_desaforo:
    scene bg casa
    with fade


    show marido neutro:
        yalign 0.2

    e "você não vê que fiquei o dia inteiro dando duro"
    e "trabalhando pra ajudar a colocar comido aqui dentro de casa, assim como você"
    e "e ainda estudando pra tentar um futuro melhor pra gente"

    show marido zangado
    e "você acha que sou obrigada?"


    show marido zangado at left:
        yalign 0.2

    "..."
    jump outro_dia

label outro_dia:
    scene bg bairro
    with fade


    "seu karma atual é [karma]"


label briga_com_marido_leve:
    scene bg sala
    with fade

    show marido neutro at left:
        yalign 0.2

    m "Chegando em casa tarde de novo?"

    m "Cheguei em casa cansado, com fome"
    m "Trabalhei o dia inteiro"


    show marido zangado at left:
        yalign 0.2




    show marido neutro at left:
        yalign 0.2


    menu:

        m "Não acha que o minimo seria ter minha esposa me esperando? E algo gostoso na cozinha para comer..."

        "Acho um absurdo ter que escutar isso":
            $ karma += 5
            jump vou_preparar_algo

        "Desculpa meu bem, tambem estou cansada":

            $ karma -= 5
            jump vou_preparar_algo


        "Tem comida na geladeira, porque não esquentou no microondas?":

            $ karma += 5
            jump tem_comida_na_geladeira

label vou_preparar_algo:
    scene bg sala
    with fade


    show marido neutro:
        yalign 0.2

    m "É por isso que eu te amo"


    show marido satisfeito:
        yalign 0.2


    m "Obrigado meu bem"

    jump dia2

label tem_comida_na_geladeira:
    scene bg sala


    show marido zangado:
        yalign 0.2

    m "Tambem não precisa me tratar desse jeito né?"


    show marido neutro:
        yalign 0.2


    m "Se não quer cozinhar tudo bem"
    m "Eu me viro aqui"

    hide marido

    jump dia2

label dia2:
    scene bg sala
    with fade

    "..."
    jump briga_com_marido_seria


label briga_com_marido_seria:

    scene bg sala
    with fade

    show marido zangado:
        yalign 0.2

    m "zangado"

    show marido gritando

    m "gritando"


    show marido neutro

    m "..."

    menu:

        "Mesmo exausta, seu marido te cobra que ainda faça cumpra com as obrigações da casa"

        "Você abaixa a cabeça e consente.":
            $ karma -= 5
            jump rota_passiva

        "Você responde ao desaforo":

            $ karma += 5
            jump rota_atitude

    return

    
    
