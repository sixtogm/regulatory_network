interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-"),
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+")
]

regulon = {}

for TF, gene, effect in interactions:
    if TF not in regulon:
        regulon[TF] = []
    regulon[TF].append(gene)

for TF in sorted(regulon):
    genes = sorted(regulon[TF])
    total = len(genes)
    lista_genes = ", ".join(genes)
    print("|",TF,"|", total,"|", lista_genes,"|")

