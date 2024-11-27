# Ruta Óptima: Algoritmos de Dijkstra y A* para Calcular el Camino Más Corto

Este proyecto implementa los algoritmos **Dijkstra** y **A\*** para calcular el recorrido mínimo entre dos puntos en un mapa de calles reales obtenidas de **OpenStreetMap**. Al final del proceso, se genera una imagen visual con el camino más corto trazado entre los puntos de origen y destino.

## Descripción

En este proyecto, se utilizan dos de los algoritmos de búsqueda más conocidos en el campo de la informática y la inteligencia artificial: **Dijkstra** y **A\***, para encontrar el **camino más corto** entre dos puntos en una red de calles reales.

El mapa de calles se obtiene de **OpenStreetMap (OSM)**, una base de datos libre de mapas y geolocalización. Los algoritmos de Dijkstra y A\* permiten encontrar la ruta más corta desde un punto de origen hasta un punto de destino, teniendo en cuenta las distancias entre los nodos (calles).

### ¿Cómo funciona?

1. **Obtención del mapa**: Se utiliza la API de **OpenStreetMap** para descargar datos geográficos, como calles y caminos entre diferentes ubicaciones.
2. **Cálculo del camino más corto**: El algoritmo de **Dijkstra** encuentra el camino más corto entre dos nodos, mientras que **A\*** mejora este proceso al usar una heurística para hacer la búsqueda más eficiente.
3. **Generación de la imagen**: Una vez que el algoritmo encuentra el camino más corto, se genera una imagen que muestra el mapa con la ruta más corta trazada entre el origen y el destino.

## Requisitos

Este proyecto requiere las siguientes librerías de Python para funcionar correctamente:

- **networkx**: Para manejar el grafo y los algoritmos de búsqueda de caminos.
- **matplotlib**: Para generar la visualización gráfica de la ruta.
- **osmnx**: Para obtener datos geográficos de OpenStreetMap.
- **numpy**: Para operaciones matemáticas y manejo de matrices.
- **requests**: Para interactuar con la API de OpenStreetMap si es necesario.
- **pillow**: Para manipular imágenes y guardar los resultados.

Puedes instalar las dependencias utilizando un entorno virtual y el archivo `requirements.txt`.

### Instalación

1. **Crear entorno virtual**
  Ejecuta este código
   #### En Windows:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Instalar las dependencias**

  Instala las librerías necesarias desde el archivo requirements.txt:
  
  ```bash
  pip install -r requirements.txt
  ```
