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
El programa debe de recibir 2 argumwntos, el archivo de entrada y el archivo de salida