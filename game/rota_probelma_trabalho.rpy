label rota_problema_trabalho:
    scene bg trabalho1
    with fade

    show chefe1 zangado at left with vpunch:
        yalign 0.2


    chefe1 "É isso aqui que você chama de relatório???"


    chefe1 "Não tem nada do que eu preciso aqui"


    show chefe1 neutro at left:
        yalign 0.2

    chefe1 "Mocinha"

    extend ", se você quiser continuar por aqui, vou precisar que você vista a camisa da empresa!"

    show chefe1 zangado at left with vpunch:
        yalign 0.2


    show mulher_trabalho surpresa at right:
        yalign 0.2

    menu:
        chefe1 "Você não tem capacidade de fazer um simples relatório sozinha?"

        "Relatório de balanço não é minha responsabilidade":


            show mulher_trabalho neutra at right:
                yalign 0.2
            
            $ karma_autoestima += 10
            personagem "Olha, esses relatórios que você me pediu com urgência..."
            extend "\n Em cima da hora"
            personagem "Nem são de responsabilidade do meu departamento"
            show chefe1 zangado at left:
                yalign 0.2

            personagem "E eu visto a camisa da empresa sim!"
            personagem "O maior exemplo disso foi eu ter ficado mais de duas horas além do expediente ontem pra resolver isso!"

            jump vai_continuar_na_empresa
            
        "Vou tentar melhorar":


            show mulher_trabalho triste at right:
                yalign 0.2
            
            $ karma_autoestima -= 10
            personagem "Desculpe"

            show chefe1 satisfeito at left:
                yalign 0.2
            extend ", vou tentar fazer melhor"
            show chefe1 neutro at left:
                yalign 0.2
            personagem "Irei agora mesmo revisar estes relatórios"

            show chefe1 satisfeito at left:
                yalign 0.2

            chefe1 "Esterei esperando por eles as 14 horas, na minha mesa"

        "Eu fiquei até depois do expediente pra conseguir entregar esses relatórios":


            show mulher_trabalho neutra at right:
                yalign 0.2
            
            $ karma_autoestima += 10
            personagem "Olha, eu fiquei até depois do expediente ontem para poder entregar esses relatórios"
            personagem "Eu assumi essa demanda devido a urgencia"
            personagem "Se não esta bom"


            show chefe1 pena at left:
                yalign 0.2
            extend ", podemos melhorar"
            personagem "Mas não acho legal você falar assim comigo"


            jump vai_continuar_na_empresa





    jump vai_continuar_na_empresa


label vai_continuar_na_empresa:

    scene bg trabalho1
    with fade


    show chefe1 neutro at left with vpunch:
        yalign 0.2

    chefe1 "Mocinha, com esse comportamento"

    extend ", eu não sinto que esta havendo uma colaboração aqui"
    

    menu:
        chefe1 "Você precisa dar um jeito nesse seu comportamento mocinha"

        "Não tem nenuma mocinha aqui!":

            $ karma_autoestima += 10
            show mulher_trabalho neutra at right with hpunch:
                size (1750,1750)
                yalign 0.2
            personagem "Esse emprego não vale isso tudo não"
            personagem "Eu não me capacitei"
            personagem "Eu não entrego meu suor aqui"

            extend ", pra ficar ouvindo isso"
            personagem "Ser tratada dessa maneira"

            show chefe1 zangado at left:
                yalign 0.2

            chefe1 "Então..."


            personagem "Então eu me demito"

            jump me_demito


        "Isso não vai se repetir":

            $ karma_autoestima -= 20
            show mulher_trabalho triste at right:
                yalign 0.2

            personagem "Vou me adequar ao que a empresa espera de mim"

            jump vou_me_adequar


label me_demito:

    scene bg trabalho1
    with fade

    show chefe1 neutro at left:
                yalign 0.2

    chefe1 "Entendo que você esteja cansada"

    chefe1 "Você deve estar confusa"
    show chefe1 satisfeito at left:
                yalign 0.2

    menu:

        chefe1 "Esta esquecendo quem precisa de quem aqui"

        "Você quem está confundindo as coisas aqui":


            show mulher_trabalho triste at right:
                yalign 0.2

            personagem "Para tratar uma funcionária desse jeito"

            extend "\nQuem está confuso aqui é você"


            personagem "Eu me demito!"

    hide chefe1

    scene bg demissao
    with fade

    "Não foi uma decisão fácil"

    "Mas aquele ambiente de trabalho não estava te fazendo bem"

    jump final_demissao



label vou_me_adequar:
    scene bg trabalho1
    with fade

    show mulher_trabalho neutra at right:
                yalign 0.2

    "Você tenta se ajustar ao que a empresa espera de você"


    hide mulher_trabalho
    show mulher_trabalho2 neutra at right:
                yalign 0.2

    "Mas nunca é o suficiente"



    "Aos poucos você deixa de se sentir como você mesma"

    "Você sabe que em algum ponto"


    show mulher_trabalho2 triste at right:
                yalign 0.2

    extend ", você se perdeu"

    jump final_na_empresa




