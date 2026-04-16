import os
import sys
import argparse

# ================================================================================================   
# Lectura del archivo y construcción de interactions
# ================================================================================================
# Responsabilidad: Leer el archivo de interacciones y construir una listga de tuplas que contenga la información de cada regulador.
# Entrada: Un archivo TSV con las interacciones entre reguladores y genes, donde cada línea contiene información sobre un regulador, un gen y el efecto de la regulación (activación o represión).
# Salida: Una lista de tuplas (TF, gene, effect).
# ================================================================================================

def load_interactions(filename):
    """Carga las interacciones desde un archivo TSV y devuelve una lista de tuplas (TF, gene, effect).

    Args:
        filename (str): Ruta al archivo TSV que contiene las interacciones.

    Returns:
        list: Una lista de tuplas (TF, gene, effect) que representan las interacciones entre reguladores y genes.
    """
    interactions = []

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

    return interactions


# ================================================================================================
# Construcción del regulon con datos extra
# ================================================================================================
# TODO: Extraer construccion del regulon build_regulon()
# ================================================================================================
#  Responsabilidad: Se encarga de crear el regulon a partir de la lista de interacciones.
#  Entrada: Lista de interacciones (TF, gene, effect) obtenida del archivo TSV.
#  Salida: El diccionario "regulon".
# ================================================================================================

def build_regulon(interactions):
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
    return regulon


# =================================================================================
# Generación de la salida
# =================================================================================
# TODO: Extraer escritura de esta seccion a una funcion write_summary()
# =================================================================================
# Responsabilidad: Generar un archivo txt con los resultados calculando el tipo de regulador para cada TF antes de escribirlo.
# Entrada: El regulon hecho en el bloque de condigo anterior.
# Salida: Archivo txt con los resultados y aparte se imprimen los resultados en la terminal.
# =================================================================================

def write_summary(regulon):
    output_file = sys.argv[2]
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, "w") as out:
        out.write("TF\tTotal genes\tActivados\tReprimidos\tGenes\tTipo\n")
        
        print("TF\tTotal genes\tActivados\tReprimidos\tGenes\tTipo")
        
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
        
            linea = (f"{TF}\t{total}\t{act}\t{rep}\t{lista_genes}\t{tipo}")
            out.write(linea + "\n")
            print(linea)


def main ():


    # TODO: Extraer argumentos de linea de comandos y tener la funcion de leer_argumentos() 
    parser = argparse.ArgumentParser(description="Resumen de regulones a partir de un archivo TSV.")

    #Definir argumentos
    parser.add_argument("input_file", help="Archivo TSV de entrada con interacciones TF-gene.")
    parser.add_argument("output_file", help="Archivo TSV de salida con resumen del regulon.")
    parser.add_argument("--min_genes", type=int, default=1, help="Número mínimo de genes regulados para incluir un TF en el resumen.")
    args = parser.parse_args()

    # TODO: Validar que el archivo de entrada existe y es legible antes de intentar cargarlo.

    # Cargar interacciones
    interactions = load_interactions(filename=args.input_file)
    
    # Construir regulon
    regulon = build_regulon(interactions)
    
    # Generar salida
    write_summary(regulon)


if __name__ == "__main__":
    main()
