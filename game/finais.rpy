
label final_demissao:

#karma_autoestima = 0
#default karma_estudo = 0

#default karma_relacionamento = 0

    if karma_relacionamento < 0:
        
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
        extend  "Você vai ver que era disso que você estava precisando"

        if karma_autoestima > 0:
            jump final_pequena_empreendedora
        else:
            jump final_procura_novo_emprego



    return

label final_na_empresa:
    #já foi finalizado

    return


label final_demissao_manteve_relacionamento:

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

    extend ", procurar outro emprego não era uma necessidade imediata"

    


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

    return


label final_procura_novo_emprego:

    return


label final_avisos:

    return