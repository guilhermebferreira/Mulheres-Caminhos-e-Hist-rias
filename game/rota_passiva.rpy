label rota_passiva:
    scene bg sala
    with fade

    show marido neutro

    m "..."

    m "Você esta sobrecarregada"
    m "Qualque um consegue enxergar isso"
    show marido satisfeito
    m "Conciiar trabalho e faculdade está sendo demais para você"
    show marido neutro
    m "Basta dar uma olhada nessa casa que a gente vê que você não esta dando conta"


    menu:

        m"Esta claro que ou você trabalha, ou você estuda"

        "Acho que vou trancar a faculdade":
            $ karma -= 15
            jump rota_passiva_pede_demissao

        "Acho que vou pedir demissão":
            $ karma -= 10
            jump rota_passiva_tranca_faculdade

        "Você responde ao desaforo":

            $ karma += 5
            jump rota_cabeca_erguida
