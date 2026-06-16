def coloracao_gulosa(G):
    """
    Atribui turnos (cores) às zonas de forma que nenhuma
    zona vizinha tenha o mesmo turno.
    Retorna: dict {zona: turno}
    """
    coloracao = {}

    for no in G.nodes():
        cores_vizinhos = {coloracao[v] for v in G.neighbors(no) if v in coloracao}

        turno = 0
        while turno in cores_vizinhos:
            turno += 1

        coloracao[no] = turno

    return coloracao
