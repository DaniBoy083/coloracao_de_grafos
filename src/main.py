from grafo import criar_grafo_cidade
from algoritmo import coloracao_gulosa
from validacao import validar_coloracao
from visualizacao import visualizar, NOMES_TURNOS


def main():
    print("=" * 55)
    print("  RouteMap — Coloração de Grafos")
    print("  Otimização de Turnos de Coleta Urbana")
    print("=" * 55)

    G = criar_grafo_cidade()
    print(f"\n📍 Zonas no grafo : {G.number_of_nodes()}")
    print(f"🔗 Adjacências    : {G.number_of_edges()}")

    coloracao = coloracao_gulosa(G)

    print("\n📅 Atribuição de Turnos:")
    for zona, turno in coloracao.items():
        print(f"   {zona:<12} → {NOMES_TURNOS[turno]}")

    num_turnos = max(coloracao.values()) + 1
    print(f"\n🎨 Turnos necessários : {num_turnos}")

    conflitos = validar_coloracao(G, coloracao)
    if conflitos:
        print(f"\n⚠️  CONFLITOS DETECTADOS: {conflitos}")
    else:
        print("✅ Nenhum conflito! Todas as zonas vizinhas têm turnos distintos.")

    visualizar(G, coloracao)


if __name__ == "__main__":
    main()
