# RouteMap — Coloração de Grafos para Otimização de Turnos Urbanos

Sistema de agendamento automático de turnos de coleta urbana baseado em **Coloração de Grafos**. Cada zona da cidade é modelada como um nó, e zonas vizinhas recebem automaticamente turnos distintos — eliminando conflitos operacionais sem intervenção manual.

---

## Contexto

Empresas de logística urbana que operam coleta seletiva em múltiplas zonas enfrentam um problema clássico de conflito de recursos: duas zonas adjacentes não podem receber o mesmo turno de coleta, pois compartilham infraestrutura, rotas ou equipes.

O problema é equivalente à **Coloração de Grafos**: dado um grafo onde cada nó é uma zona e cada aresta representa uma restrição de adjacência, encontrar a atribuição de turnos (cores) que garanta que nenhuma aresta conecte dois nós de mesma cor, usando o menor número de turnos possível.

---

## Estrutura do Projeto

```
routemap/
├── main.py           # Ponto de entrada — orquestra o pipeline completo
├── grafo.py          # Construção do grafo de zonas urbanas
├── algoritmo.py      # Algoritmo guloso de coloração
├── validacao.py      # Verificação de conflitos na coloração gerada
└── visualizacao.py   # Renderização do grafo com matplotlib
```

---

## Módulos

### `grafo.py`

Constrói o grafo com `networkx`. Cada zona urbana vira um nó; cada fronteira compartilhada entre zonas vira uma aresta.

```python
from grafo import criar_grafo_cidade

G = criar_grafo_cidade()
# G.number_of_nodes() → 8
# G.number_of_edges() → 12
```

**Zonas modeladas:** Centro, Bairro A, Bairro B, Bairro C, Bairro D, Bairro E, Bairro F, Bairro G.

Para adicionar novas zonas, basta inserir o nó e as arestas correspondentes — o algoritmo recolore automaticamente.

---

### `algoritmo.py`

Implementa o **Algoritmo Guloso de Coloração** do zero, sem usar `nx.greedy_color`.

```python
from algoritmo import coloracao_gulosa

coloracao = coloracao_gulosa(G)
# → {"Centro": 0, "Bairro A": 1, "Bairro B": 2, ...}
```

**Lógica:**

```
Para cada nó do grafo:
    1. Coletar os turnos já atribuídos aos vizinhos
    2. Atribuir o menor turno não usado pelos vizinhos
```

**Complexidade:** O(V + E) — linear no número de vértices e arestas.

> O algoritmo guloso não garante o número cromático ótimo χ(G), mas é eficiente e suficiente para grafos esparsos como malhas urbanas. A ordem de iteração dos nós influencia o resultado.

---

### `validacao.py`

Verifica a integridade da coloração gerada. Percorre todas as arestas e checa se algum par de vizinhos recebeu o mesmo turno.

```python
from validacao import validar_coloracao

conflitos = validar_coloracao(G, coloracao)
# → [] (lista vazia = sem conflitos)
```

Retorna uma lista de tuplas `(zona_a, zona_b)` para cada aresta em conflito. Em uma coloração válida, a lista sempre será vazia.

---

### `visualizacao.py`

Renderiza o grafo colorido usando `matplotlib` e `networkx`. Cada turno recebe uma cor distinta; a legenda exibe o nome do turno correspondente.

```python
from visualizacao import visualizar

visualizar(G, coloracao)
# → exibe o grafo e salva "routemap_grafo.png"
```

**Paleta de turnos:**

| Cor | Turno |
|-----|-------|
| 🔴 `#E63946` | Turno Manhã |
| 🟢 `#2A9D8F` | Turno Tarde |
| 🟡 `#E9C46A` | Turno Noite |
| 🔵 `#264653` | Turno Madrugada |
| 🟠 `#F4A261` | Turno Extra A |
| 🩵 `#A8DADC` | Turno Extra B |

---

### `main.py`

Orquestra o pipeline completo: criação do grafo → coloração → validação → visualização.

```python
python main.py
```

Saída esperada no terminal:

```
=======================================================
  RouteMap — Coloração de Grafos
  Otimização de Turnos de Coleta Urbana
=======================================================

📍 Zonas no grafo : 8
🔗 Adjacências    : 12

📅 Atribuição de Turnos:
   Centro       → Turno Manhã
   Bairro A     → Turno Tarde
   Bairro B     → Turno Noite
   ...

🎨 Turnos necessários : 3
✅ Nenhum conflito! Todas as zonas vizinhas têm turnos distintos.
```

---

## Instalação

**Pré-requisitos:** Python 3.8+

```bash
pip install -r requirements.txt
```

---

## Execução

```bash
# ir para a pasta src
cd ./src
# e depois
python -m main.py
```

O grafo colorido será exibido em janela e salvo como `routemap_grafo.png` no diretório atual.

---

## Fundamentos Teóricos

### Coloração de Grafos

Dado um grafo G = (V, E), uma **coloração válida** é uma função:

```
c: V → {1, 2, ..., k}
```

tal que para toda aresta `(u, v) ∈ E`: `c(u) ≠ c(v)`

O menor `k` para o qual isso é possível é chamado de **número cromático** χ(G).

### Algoritmo Guloso

```python
def coloracao_gulosa(G):
    coloracao = {}
    for no in G.nodes():
        cores_vizinhos = {coloracao[v] for v in G.neighbors(no) if v in coloracao}
        turno = 0
        while turno in cores_vizinhos:
            turno += 1
        coloracao[no] = turno
    return coloracao
```

### Propriedades relevantes

- **NP-difícil** no caso geral determinar χ(G), mas heurísticas gulosas funcionam bem na prática
- **Teorema das 4 Cores:** todo grafo planar é colorível com no máximo 4 cores — malhas urbanas são sempre grafo planar
- **Grafos esparsos** (como malhas de cidades) permitem colorações próximas do ótimo com o algoritmo guloso

---

## Aplicações da Coloração de Grafos

O mesmo modelo resolve problemas em outras áreas:

- **Redes de frequência** — antenas próximas não podem usar a mesma frequência (4G/5G)
- **Grade de horários** — provas com alunos em comum não podem ocorrer ao mesmo tempo
- **Compiladores** — alocação de registradores de CPU
- **Bioinformática** — análise de sequências de DNA sem sobreposição
- **Cartografia** — países vizinhos em cores distintas (caso histórico que motivou o Teorema das 4 Cores)