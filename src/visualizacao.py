import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx


PALETA = ["#E63946", "#2A9D8F", "#E9C46A", "#264653", "#F4A261", "#A8DADC"]
NOMES_TURNOS = ["Turno Manhã", "Turno Tarde", "Turno Noite",
                "Turno Madrugada", "Turno Extra A", "Turno Extra B"]


def visualizar(G, coloracao):
    cores_nos = [PALETA[coloracao[n] % len(PALETA)] for n in G.nodes()]
    pos = nx.spring_layout(G, seed=42)

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("#0F172A")
    ax.set_facecolor("#0F172A")

    nx.draw_networkx_edges(G, pos, ax=ax, edge_color="#475569", width=2, alpha=0.7)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=cores_nos,
                           node_size=900, edgecolors="white", linewidths=2)
    nx.draw_networkx_labels(G, pos, ax=ax, font_color="white",
                            font_size=8, font_weight="bold")

    num_cores = max(coloracao.values()) + 1
    legend = [
        mpatches.Patch(color=PALETA[i], label=NOMES_TURNOS[i])
        for i in range(num_cores)
    ]
    ax.legend(handles=legend, loc="upper left", framealpha=0.2,
              labelcolor="white", facecolor="#1E293B", edgecolor="#334155")

    ax.set_title("RouteMap — Coloração de Turnos de Coleta Urbana",
                 color="white", fontsize=13, pad=15)
    ax.axis("off")

    plt.tight_layout()
    plt.savefig("routemap_grafo.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("\n✅ Imagem salva em: routemap_grafo.png")
