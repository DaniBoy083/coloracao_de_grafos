import networkx as nx


def criar_grafo_cidade():
    """Cria grafo representando zonas urbanas e suas adjacências."""
    G = nx.Graph()

    zonas = [
        "Centro", "Bairro A", "Bairro B", "Bairro C",
        "Bairro D", "Bairro E", "Bairro F", "Bairro G"
    ]
    G.add_nodes_from(zonas)

    arestas = [
        ("Centro", "Bairro A"), ("Centro", "Bairro B"), ("Centro", "Bairro C"),
        ("Bairro A", "Bairro B"), ("Bairro A", "Bairro D"),
        ("Bairro B", "Bairro C"), ("Bairro B", "Bairro E"),
        ("Bairro C", "Bairro F"), ("Bairro D", "Bairro E"),
        ("Bairro E", "Bairro F"), ("Bairro E", "Bairro G"),
        ("Bairro F", "Bairro G"),
    ]
    G.add_edges_from(arestas)

    return G
