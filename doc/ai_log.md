### Durante la creacion de este codigo el asistente "TutorPy: Tu guía en Python paso a paso" de la compañia ChatGPT, creado por Lic. Salgado fue utilizado en las siguientes ocasiones:

1. Se le pregunto por una manera mediante la cual el codigo actual, pudiera reproducir una salida del tipo | TF | Total genes | Activados | Reprimidos | Tipo |.
````python
interactions = [ 
    ("AraC", "araA", "+"), 
    ("AraC", "araB", "-"), 
    ("LexA", "recA", "-"), 
    ("CRP", "lacZ", "+"), 
    ("CRP", "lacY", "+") 
] 

regulon = {}

actividad = {} 

for TF, gene, effect in interactions: 
    if TF not in regulon: 
        regulon[TF] = [] 
    regulon[TF].append(gene) 
    if effect not in actividad: 
        actividad[TF]=[] 
        actividad[TF].append(effect) 
        
for TF in sorted(regulon): 
    genes = sorted(regulon[TF]) 
    total = len(genes) 
    lista_genes = ", ".join(genes) 
    print("|",TF,"|", total,"|", lista_genes,"|")````

La IA sugirio:

````python
interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-"),
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+")
]

resumen = {}

for TF, gene, effect in interactions:
    if TF not in resumen:
        resumen[TF] = {
            "total": 0,
            "activados": 0,
            "reprimidos": 0
        }
    
    resumen[TF]["total"] += 1
    
    if effect == "+":
        resumen[TF]["activados"] += 1
    elif effect == "-":
        resumen[TF]["reprimidos"] += 1

# imprimir tabla
print("| TF | Total genes | Activados | Reprimidos | Tipo |")

for TF in sorted(resumen):
    total = resumen[TF]["total"]
    act = resumen[TF]["activados"]
    rep = resumen[TF]["reprimidos"]
    
    # determinar tipo
    if act > 0 and rep > 0:
        tipo = "dual"
    elif act > 0:
        tipo = "activador"
    else:
        tipo = "represor"
    
    print(f"| {TF} | {total} | {act} | {rep} | {tipo} |")
````

