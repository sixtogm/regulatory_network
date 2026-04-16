import argparse

parser = argparse.ArgumentParser(description="Resumen de regulones a partir de un archivo TSV.")

# Definir argumentos 
parser.add_argument("input_file", help="Archivo TSV de entrada con interacciones TF-gene.")
parser.add_argument("output_file", help="Archivo TSV de salida con resumen del regulon.")

parser.add_argument("--min_genes", type=int, default=1, help="Número mínimo de genes regulados para incluir un TF en el resumen.")

args = parser.parse_args()

print(args)

print(f"Archivo de entrada: {args.input_file}")
print(f"Archivo de salida: {args.output_file}")
print(f"Número mínimo de genes regulados: {args.min_genes}")