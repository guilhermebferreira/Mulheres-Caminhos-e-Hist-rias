

label rota_passiva:
    scene bg sala
    with fade

    show marido neutro:
        yalign 0.2

    marido "..."

    marido "Você esta sobrecarregada"
    marido "Qualque um consegue enxergar isso"
    show marido satisfeito:
        yalign 0.2
    marido "Conciiar trabalho e faculdade está sendo demais para você"
    
    show marido neutro:
    
    marido "Basta dar uma olhada nessa casa que a gente vê que você não esta dando conta"


    menu:

        marido"Esta claro que ou você trabalha, ou você estuda"

        "Acho que vou trancar a faculdade":
            $ karma -= 15
            jump rota_passiva_pede_demissao

        "Acho que vou pedir demissão":
            $ karma -= 10
            jump rota_passiva_tranca_faculdade

        "Você responde ao desaforo":

            $ karma += 5
            jump rota_atitude

label rota_passiva_pede_demissao:
    scene bg centro
    with fade

    "No dia seguinte"

    extend ", você foi ao centro apenas para pedir demissão"

    scene bg trabalho

    show chefe1 neutro

    menu:

        chefe1 "Tem certeza de que é isso mesmo que você quer fazer?"

        "Sim, eu tenho":
            $ karma -= 20

    chefe1 "é uma pena..."
    chefe1 "Boa sorte na sua jornada"



label rota_passiva_tranca_faculdade:
    scene bg centro
    with fade


    "No dia seguinte"

    extend ", você foi ao centro apenas para protocolar o trancamento do curso"

    scene bg aula

    "Não fo nem um pouco fácil preencher aquele formulário"