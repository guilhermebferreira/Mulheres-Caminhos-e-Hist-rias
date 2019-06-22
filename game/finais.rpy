
label final_demissao:

#karma_autoestima = 0
#default karma_estudo = 0

#default karma_relacionamento = 0

    if karma_relacionamento <= 0:
        
        scene bg bairro
        with fade 
        "Você não esta acostumada a ficar em casa em um dia útil"

        scene bg sala
        with fade 


        show mulher_trabalho triste at right:
                    yalign 0.2


        "É dificil se sentir bem desse jeito"

        if karma_estudo > 0:
            jump final_empresaria
        elif karma_autoestima > 0:
            jump final_pequena_empreendedora
        else:
            jump final_procura_novo_emprego

    else:


        scene bg bairro
        with fade 
        "Você não esta acostumada a ficar em casa em um dia útil"

        scene bg sala
        with fade 


        show mulher_trabalho triste at right:
                    yalign 0.2


        
        show marido neutro at left:
                    yalign 0.2
        marido "Não fique assim..."

        show marido satisfeito at left:
                    yalign 0.2
        marido "Agora você tem mais tempo pra casa"

        show mulher_trabalho surpresa at right:
                    yalign 0.2
        extend  "\nVocê vai ver que era disso que você estava precisando"

        if karma_autoestima > 0:
            jump final_pequena_empreendedora
        else:

            "Você até tenta se acostumar a finar em casa..."
            jump final_procura_novo_emprego



    return

label final_na_empresa:

    $ karma_relacionamento = 1

    if karma_relacionamento > 0:

        scene bg sala
        with fade 


        show mulher_trabalho2 triste at right:
            yalign 0.2

        "Você tem mais tempo em casa"
        extend ", \nmas isso não parece ser o suficiente"
        scene bg trabalho
        with fade 


        show mulher_trabalho2 triste at right:
            yalign 0.2

        "A rotina te deixa cada vez mais triste"


        "Você ouve falar sobre o Centro de Valorização da Vida"


        show mulher_trabalho2 neutra at right:
            yalign 0.2

        personagem "CVV: 188"
        extend "...\n talvez eu deva ligar"

        hide mulher_trabalho2


        jump final_avisos




    else:
        #já foi finalizado
        jump final_avisos

    return



label final_empresaria:


    scene bg bairro
    with fade 

    "Você decidiu que ficar parada não era uma opção"

    show mulher_trabalho triste at right:
                    yalign 0.2

    "Como você tinha algumas economias"


    show mulher_trabalho surpresa at right:
                    yalign 0.2

    extend ", \nprocurar outro emprego não era uma necessidade imediata"

    


    scene bg escola
    with fade 

    show mulher_trabalho neutra at right:
                    yalign 0.2


    "Você usou tudo que passou nos últimos dias como combustivel"

    "E se dedicou completamente em buscar qualificação proficional"

    "A remcompensa não veio de um dia pro outro"


    scene bg chefe_mulher
    with fade 

    show mulher_trabalho neutra at left:
                    yalign 0.2

    "Mas você chegou lá!"


    show mulher_trabalho sorrindo at left:
                    yalign 0.2
    "E tem muito orgulho da mulher que se tornou"

    personagem "Não há nada que você não possa fazer"

    return

label final_pequena_empreendedora:


    scene bg bairro
    with fade 

    "Ficar alguns dias em casa te fez bem"
    scene bg sala
    with fade 

    show mulher_trabalho neutra at right:
                    yalign 0.2

    "Você se conectou melhor com a comunidade a sua volta"

    "Mas você não ficou parada"

    scene bg cozinha
    with fade 

    "Para manter a mente ocupada, você passou bastante tempo na cozinha"

    "Os bolos que você fez, fizeram sucesso na vizinhança"

    scene bg bairro
    with fade 

    show mulher_trabalho sorrindo at right:
                    yalign 0.2

    "Você percebeu nisso uma oportunidade de negocio"

    personagem "Talvez minha realização profissional não estivesse onde eu estava buscando inicialmente!"

    jump final_avisos


label final_procura_novo_emprego:


    scene bg bairro
    with fade 

    "Você decidiu que ficar parada não era uma opção"
    

    scene bg centro
    with fade 


    show mulher_trabalho neutra at right:
        yalign 0.2

    "Atualizou o seu curriculo e partiu pra luta"

    jump final_avisos




label final_avisos:

    "Se você já passou "
    extend ",\n está passando"

    extend "\n ou conhece alguém que passe por qualquer tipo de abuso"

    "Busque ajuda"

    "Assédio, é sempre algo grave!"

    extend "\nDenuncie!"

    "Delegacias de Atendimento à Mulher: 180"

    extend "\nDelegacia da Mulher no DF: 61 3244-3400"


    "Disque-Denúncia: 181"


    "Não importa pelo que você esteja passando"

    extend "\nOu com o que você esteja lidando"

    extend "\n Sempre haverá alguem para te ouvir"

    "Centro de Valorização da Vida: 188"

    extend "\nCVV Brasília: (61) 3326-4111"

    "Busque ajuda, sua vida importa"

    extend "\nNão fique sozinha. Estamos com você!"

    return
 