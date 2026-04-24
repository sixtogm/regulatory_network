# Casos de prueba

## Caso 1

Entrada:

AraC araA +
AraC araB -

Salida esperada:

AraC 2 araA, araB

## Command Line Interface (CLI)
Caso: Correr el programa con paso de argumentos 

Entrada;

```bash
uv run python regulon_summary.py input.txt output.txt
```

Resultado:
El progama lea el archivo de entrada y genere el resultado con el nombre que se le paso como argumento.

## Manejo de Errores en Lectura

### Caso 1: Archivo de entrada no existe

Entrada:

```bash
python regulon_summary.py archivo_inexistente.tsv output.txt
```

Salida esperada:

```
Error: El archivo de entrada 'archivo_inexistente.tsv' no existe.
```

Resultado:
El programa detecta que el archivo no existe y termina con exit code 1 antes de intentar procesarlo.

### Caso 2: Archivo de entrada sin permisos de lectura

Entrada:

```bash
python regulon_summary.py archivo_sin_permisos.tsv output.txt
```

Salida esperada:

```
Error: No se puede leer el archivo de entrada 'archivo_sin_permisos.tsv'.
```

Resultado:
El programa verifica los permisos antes de leer y termina con exit code 1 si no tiene permisos.

### Caso 3: Error al leer archivo durante procesamiento

Entrada:

Archivo TSV con encoding incorrecto o datos corruptos.

```bash
python regulon_summary.py datos_corruptos.tsv output.txt
```

Salida esperada:

```
Error: Error al leer el archivo 'datos_corruptos.tsv': [detalles del error]
```

Resultado:
El programa captura la excepción OSError durante la lectura y muestra un mensaje descriptivo, terminando con exit code 1.

## Manejo de Errores en Escritura

### Caso 1: Directorio de salida en ruta inválida

Entrada:

```bash
python regulon_summary.py data/raw/NetworkRegulatorGene.tsv Z:\nonexistent\path\output.txt
```

Salida esperada:

```
Error al crear el directorio 'Z:\nonexistent\path': [WinError 3] El sistema no puede encontrar la ruta especificada
```

Resultado:
El programa intenta crear el directorio, detecta que la ruta es inválida, lanza RuntimeError y termina con exit code 1.

### Caso 2: Sin permisos para escribir en directorio

Entrada:

```bash
python regulon_summary.py data/raw/NetworkRegulatorGene.tsv /root/protected_dir/output.txt
```

Salida esperada:

```
Error: No se tiene permiso para crear el directorio '/root/protected_dir'.
```

Resultado:
El programa captura PermissionError al intentar crear el directorio y muestra un mensaje explicativo, terminando con exit code 1.

### Caso 3: Sin permisos para escribir en archivo existente

Entrada:

Archivo de salida con permisos de solo lectura en un directorio accesible.

```bash
python regulon_summary.py data/raw/NetworkRegulatorGene.tsv archivo_readonly.txt
```

Salida esperada:

```
Error: No se tiene permiso para escribir en el archivo 'archivo_readonly.txt'.
```

Resultado:
El programa captura PermissionError al intentar escribir y muestra un mensaje descriptivo, terminando con exit code 1.

## Caso Exitoso:

### Ejecución normal con datos válidos

Entrada:

```bash
python regulon_summary.py data/raw/NetworkRegulatorGene.tsv results/regulon_output.txt
```

Resultado esperado:
- Archivo results/regulon_output.txt se crea exitosamente
- Contiene tabla con columnas: TF, Total genes, Activados, Reprimidos, Genes, Tipo
- Salida se imprime también en terminal
- El programa termina con exit code 0
