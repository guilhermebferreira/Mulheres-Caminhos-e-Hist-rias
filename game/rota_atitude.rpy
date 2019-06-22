label rota_atitude:

    scene bg sala
    with fade


    show marido neutro at left:
        yalign 0.2

    personagem "Não esta certo isso"

    personagem "Gosto muito de você, mas..."

    show marido zangado at left:
        yalign 0.2

    personagem "Você esta pedindo que eu abra mão de muita coisa"

    personagem "Você esta pedindo..."



    extend "\nVocê esta exigindo que eu abra mão do meu futuro"

    show marido satisfeito at left:
        yalign 0.2

    menu:

        marido "Você esta apenas confusa..."

        "Não":
            personagem "Não"
            show marido zangado at left:
                yalign 0.2
            extend ", muito pelo contrario"
            personagem "Faz tempo que não tenho tanta certeza de algo"
        "Talvez":
            personagem "Talvez esteja"
            extend ", mass..."
            show marido zangado at left:
                yalign 0.2


    personagem "Você pediu que eu fizesse uma escolha."
    
    show marido neutro at left:
        yalign 0.2

    personagem "Eu fiz"
    show marido zangado at left:
        yalign 0.2

    personagem "Estou escolhendo me valorizar"
    
    

    return
