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