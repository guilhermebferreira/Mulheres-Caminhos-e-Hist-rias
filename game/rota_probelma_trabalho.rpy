label rota_probelma_trabalho:
    scene bg trabalho1
    with fade

    show chefe1 zangado with vpunch:
        yalign 0.2


    chefe1 "É isso aqui que você chama de relatório???"


    chefe1 "Não tem nada do que eu preciso aqui"


    show chefe1 neutro:
        yalign 0.2

    chefe1 "Mocinha"

    extend ", se você quiser continuar por aqui, vou precisar que você vista a camisa da empresa!"


    menu:
        chefe1 "Você não tem capacidade de fazer um simples relatório sozinha?"

        "Relatório de balanço não é minha responsabilidade":
            $karma += 1
            personagem "Olha, eses relatórios que você me pediu com urgência..."
            extend "\n Em cima da hora"
            personagem "Nem são de responsabilidade do meu departamento"
            show chefe1 zangado:
                yalign 0.2

            personagem "E eu visto a camisa da empresa sim!"
            personagem "O maior exemplo disso foi eu ter ficado mais de duas horas além do expediente ontem pra resolver isso!"
            
        "Vou tentar melhorar":
            $karma -= 1
            personagem "Desculpe"

            show chefe1 satisfeito:
                yalign 0.2
            extend ", vou tentar fazer melhor"
            show chefe1 neutro:
                yalign 0.2
            personagem "Irei agora mesmo revisar estes relatórios"

            show chefe1 satisfeito:
                yalign 0.2

            chefe1 "Esterei esperando por eles as 14 horas, na minha mesa"

        "Eu fiquei até depois do expediente pra conseguir entregar esses relatórios":
            $karma += 1
            personagem "Olha, eu fiquei até depois do expediente ontem para poder entregar esses relatórios"
            personagem "Eu assumi essa demanda devido a urgencia"
            personagem "Se não esta bom"


            show chefe1 pena:
                yalign 0.2
            extend ", podemos melhorar"
            personagem "Mas não acho legal você falar assim comigo"





    return


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
    		show personagem neutro at right with hpunch:
        		yalign 0.2
        	personagem "Esse emprego não vale isso tudo não"
        	personagem "Eu não me capacitei"
        	personagem "Eu não entrego meu suor aqui"

        	extend ", pra ficar ouvindo isso"
        	personagem "Ser tratada dessa maneira"


        "Isso não vai se repetir":
    		show personagem triste at right:
        		yalign 0.2


