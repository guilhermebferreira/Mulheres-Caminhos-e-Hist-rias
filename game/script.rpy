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


    show voce cansada



    jump voltando_pra_casa





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
 


label voltando_pra_casa:
    scene bg bairro
    with fade

    e "Estou exausta"

    e "Acho que não faria mal deixar de ir na faculdade só por hoje"

    menu:
        e "Então, será que..."

        "Vou direto pra casa, descançar um pouco seria bom":
            jump volta_pra_casa

        "Melhor ir pra faculdade":
            jump vai_pra_faculdade

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

    "você tira a chave da bolsa e se sente leve"

    e "É sempre bom chegar em casa!"

    jump briga_com_marido_leve



label briga_com_marido_leve:
    scene bg sala 


    m "Chegando tarde de novo?"

    show marido neutro at left:
        yalign 0.2
    m "Já são quase nove, estou morrendo de fome"

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

    m "Você sabe que eu te amo"


    m "Não sabe?"


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
    scene bg bairro
    with fade

    "um novo dia..."
    jump briga_com_marido_seria

label dia_cheio_trabalho:
    scene bg trabalho1
    with fade

    " Gina está se sentindo muito sobrecarregada. Ela acredita que por ter entrado agora, os superiores dela estão pegando muito pesado, pedindo pra ela fazer tarefas que não são da sua função"
    " e ficar até depois do seu horário de trabalho"


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

    
    
