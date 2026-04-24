# Context

Este proyecto analiza una red de regulación genética.

Los datos contienen interacciones entre factores de transcripción (TF) y genes.

Formato de los datos:

TF gene effect

Ejemplo:

AraC araA + AraC araB - LexA recA - ```

Objetivo del programa:

Generar una tabla que indique para cada TF:

- Nombre del TF (esta solumna debe estar ordenada)
- total de genes regulados
- lista de genes regulados (ordenada) 
- numero de genes activados ("+")
- numero de genes reprimidos ("-")
- Tipo de regulador:
   - "activador" si solo activa
   - "represor" si solo reprime 
   - "dual" si activa y oprime



## Actualizacion v1.1

1. Leer los datos desde un archivo
    1. El archivo tiene 7 columnas, las que vamos a utilizar son:
2. Los resultados deben de mandarse a un archivo de salida.

## Actualizacion v1.2Problema:
El programa depende de rutas fijas (hardcoded)

Numero requisito:
El programa debe de recibir 2 argumentos, el archivo de entrada y el archivo de salida

Se agregó el uso de la librería `argparse` para manejar los argumentos de línea de comandos de manera más robusta y flexible.

## Actualizacion v1.3
El programa ahora reconoce e informa ciertos errores a la hora de leer archivos y escribirlos con try&except.