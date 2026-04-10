# Algoritmo

- Lista/estructura de reguladores (sin repeticiones)
- Lista de genes del regulador (sin repeticiones)
- Recorrer todas las interacciones (linea)
- Para cada interaccion
    - Obtener el TF
    - Obtener el gen
    - Si el TF no esta en la lista de reguladores 
      - Guardar el TF en una estructura/lista
    - Si el gen no esta en la lista de genes por regulados por regulador
      - Guardar el gen asociado

- Recorrer la lista de los reguladores
  - Contar los genes de la lista de genes regulados por el TF
  - imprime regulador, conteo, lista de genes

## Actualizacion v1.1
- Leer los datos desde un archivo.
  -abrir el archivo
  -recorrer cada línea
  -limpiar la línea
  -ignorar líneas vacías
  -separar columnas
  -validar número de columnas
  -extraer TF, gene y effect
  -validar effect
  -construir la lista de interacciones
  -reutilizar el código previo para construir el regulon
  -generar el formato de salida
  -guardar los resultados en un archivo

## Actualizacion v1.2
Elprograma recibira 2 argumentos desde la linea de comandos

Flujo:

usuario --> CLI (Command Line Interface) --> main () 