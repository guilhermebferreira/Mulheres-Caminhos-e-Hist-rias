# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Personagem")
define m = Character("Marido")
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

    "seu karma atual é [karma]"


    show eileen cansada

    $ karma -= 1


    "seu karma atual é [karma]"

    e "Você esta ao mesmo tempo cansada pelo dia longo. \nE feliz por estar chegando em casa"

    # This ends the game.

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
            jump vou_pra_cozinha

        "Você responde ao desaforo":

            $ karma += 5
            jump responde_desaforo

    return

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


