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

## Actualizacion v1.1

1. Al mismo asistente de IA se le pidio a ayuda para solucionar lo siguiente:
````py
with open("results/regulon_summary_output.txt", "w") as out:
    out.write("| TF | Total genes | Activados | Reprimidos | Genes | Tipo |\n")
````

````py
for TF in sorted(regulon):
    ...
    out.write(f"| {TF} | {total} | {act} | {rep} | {lista_genes} | {tipo} |")
````

A lo que sugirio:

````py
with open("results/regulon_summary_output.txt", "w") as out:
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
        
        linea = f"| {TF} | {total} | {act} | {rep} | {lista_genes} | {tipo} |"
        
        out.write(linea + "\n")
        print(linea)
````
Su sugerencia fue aplicada pero modificada en cuanto a rutas dadas.

## Interacciones con GitHub Copilot (Asistente de Programación)

1. Se pidió implementar los dos TODO presentes en el código de `regulon_summary.py` sin modificarlo.

   El código tenía los siguientes TODO:
   - Extraer argumentos de línea de comandos a una función `leer_argumentos()`.
   - Validar que el archivo de entrada existe y es legible antes de intentar cargarlo.

   La IA implementó:
   - Creó la función `parse_arguments()` para manejar el análisis de argumentos con `argparse`.
   - Agregó validación en `main()` para verificar existencia y legibilidad del archivo de entrada.
   - Modificó `write_summary()` para aceptar `output_file` como parámetro y actualizó la llamada en `main()`.

   Código modificado:
   ````python
   def parse_arguments():
       parser = argparse.ArgumentParser(description="Resumen de regulones a partir de un archivo TSV.")
       parser.add_argument("input_file", help="Archivo TSV de entrada con interacciones TF-gene.")
       parser.add_argument("output_file", help="Archivo TSV de salida con resumen del regulon.")
       parser.add_argument("--min_genes", type=int, default=1, help="Número mínimo de genes regulados para incluir un TF en el resumen.")
       args = parser.parse_args()
       return args

   def main():
       args = parse_arguments()
       
       if not os.path.isfile(args.input_file):
           print(f"Error: El archivo de entrada '{args.input_file}' no existe.")
           sys.exit(1)
       
       if not os.access(args.input_file, os.R_OK):
           print(f"Error: No se puede leer el archivo de entrada '{args.input_file}'.")
           sys.exit(1)
       
       interactions = load_interactions(filename=args.input_file)
       regulon = build_regulon(interactions)
       write_summary(regulon, args.output_file)
   ````

## Manejo de Errores en Escritura

1. Se preguntó si ya había manejo de errores en la lectura y la escritura del código.

   - Lectura: Ya tenía un bloque try-except en `load_interactions()` que capturaba `FileNotFoundError`, `PermissionError` y `OSError`.
   - Escritura: No había manejo de errores en `write_summary()`, solo llamaba `os.makedirs()` y `open()` sin protección.

2. Se le pidio ayuda para implementar un plan para añadir el manejo de errores en la escritura:

   - Agregar un bloque try-except en `write_summary()` con el mismo patrón y nivel de detalle que `load_interactions()`.
   - Capturar `PermissionError` para errores de permisos en creación de directorio o escritura de archivo.
   - Capturar `OSError` para otros errores (rutas inválidas, espacio en disco, etc.).
   - Lanzar `RuntimeError` con mensajes descriptivos consistentes con los de lectura.
   - Asegurar que `write_summary()` estuviera dentro del try-except de `main()` (ya lo estaba).

