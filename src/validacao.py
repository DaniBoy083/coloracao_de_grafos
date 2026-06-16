def validar_coloracao(G, coloracao):
    """
    Verifica se há conflitos na coloração.
    Retorna lista de arestas com conflito (deve ser vazia).
    """
    conflitos = []
    for u, v in G.edges():
        if coloracao[u] == coloracao[v]:
            conflitos.append((u, v))
    return conflitos
