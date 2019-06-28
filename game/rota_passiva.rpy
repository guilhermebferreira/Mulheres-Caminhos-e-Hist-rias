

label rota_passiva:
    scene bg sala
    with fade

    show marido neutro at left:
        yalign 0.2

    marido "..."

    marido "Você esta sobrecarregada"
    marido "Qualquer um consegue enxergar isso"
    show marido satisfeito at left:
        yalign 0.2
    marido "Conciliar trabalho e faculdade está sendo demais para você"

    show marido neutro at left:
        yalign 0.2


    show mulher_trabalho surpresa at right:
        yalign 0.2
    
    marido "Basta dar uma olhada nessa casa que a gente vê que você não esta dando conta"


    menu:

        marido"Esta claro que ou você trabalha, ou você estuda"

        "Acho que vou trancar a faculdade":


            show mulher_trabalho triste at right:
                yalign 0.2
            personagem "Acho que vou trancar a faculdade então..."
            
            $ karma_relacionamento += 10
            $ karma_autoestima -= 10
            jump rota_passiva_tranca_faculdade

        "Acho que vou pedir demissão":


            show mulher_trabalho triste at right:
                yalign 0.2
            personagem "Acho que vou largar o emprego então"


            personagem "Me dedicar mais a nós"
            
            $ karma_relacionamento += 10
            $ karma_autoestima -= 10
            jump rota_passiva_pede_demissao

        "Você responde ao desaforo":

            $ karma_relacionamento -= 10
            $ karma_autoestima += 10
            jump rota_atitude

label rota_passiva_pede_demissao:
    scene bg centro
    with fade

    "No dia seguinte"

    extend ", você foi ao centro apenas para pedir demissão"

    scene bg trabalho

    show chefe1 neutro:
        yalign 0.2

    menu:

        chefe1 "Tem certeza de que é isso mesmo que você quer fazer?"

        "Sim, eu tenho":
            $ karma_autoestima += 10


    show chefe1 pena:
        yalign 0.2

    chefe1 "é uma pena..."
    show chefe1 neutro:
        yalign 0.2

    chefe1 "Boa sorte na sua jornada"


    jump final_demissao



label rota_passiva_tranca_faculdade:
    scene bg centro
    with fade


    "No dia seguinte"

    extend ", você acordou mais cedo para protocolar o trancamento do curso antes de ir para o trabalho..."

    scene bg aula

    "Não fo nem um pouco fácil preencher aquele formulário"


    jump rota_problema_trabalho


