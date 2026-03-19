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
        regulon[TF] = {
            "total": 0,
            "activados": 0,
            "reprimidos": 0,
            "genes": []  
        }
    
    regulon[TF]["total"] += 1
    regulon[TF]["genes"].append(gene)
    
    if effect == "+":
        regulon[TF]["activados"] += 1
    elif effect == "-":
        regulon[TF]["reprimidos"] += 1

print("| TF | Total genes | Activados | Reprimidos | Genes | Tipo |")

for TF in sorted(regulon):
    total = regulon[TF]["total"]
    act = regulon[TF]["activados"]
    rep = regulon[TF]["reprimidos"]
    
    genes_ordenados = sorted(regulon[TF]["genes"])
    lista_genes = ", ".join(genes_ordenados)
    
    if act > 0 and rep > 0:
        tipo = "dual"
    elif act > 0:
        tipo = "activador"
    else:
        tipo = "represor"
    
    print(f"| {TF} | {total} | {act} | {rep} | {lista_genes} | {tipo} |")

