import pandas as pd
import networkx as nx
import itertools

df = pd.read_csv("posts-sem-stopwords.csv")

G = nx.Graph()

# Criar arestas entre palavras que aparecem juntas
for post in df["text_clean"].dropna().tolist():
    words = post.split()
    for word1, word2 in itertools.combinations(words, 2):
        if G.has_edge(word1, word2):
            G[word1][word2]['weight'] += 1
        else:
            G.add_edge(word1, word2, weight=1)

# Exportar para CSV para o Gephi
edges = nx.to_pandas_edgelist(G)
edges.to_csv("edges.csv", index=False)
