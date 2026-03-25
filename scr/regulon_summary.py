interactions=[]

#Lectura de datos desde archivo TSV
filename= "../data/raw/NetworkRegulatorGene.tsv"

with open(filename) as f:
    for line in f:
        line=line.strip()

        if not line:
            continue
        
        if line.startswith("#"):
            continue

        if line.startswith("1)regulatorId"):
            continue

        fields=line.split("\t")

        if len(fields) <= 5:
            continue

        TF=fields[1]
        gene=fields[4]
        effect= fields[5]

        if effect not in ["+","-"]:
            continue

        interactions.append((TF, gene, effect))



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

with open("../data/results/regulon_summary_output.txt", "w") as out:
    out.write("| TF | Total genes | Activados | Reprimidos | Genes | Tipo |\n")

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
    
      linea=(f"| {TF} | {total} | {act} | {rep} | {lista_genes} | {tipo} |")
      out.write(linea +"\n")
      print(linea)

