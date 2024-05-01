import osmnx as ox
import matplotlib.pyplot as plt 

place_name = "Trujillo, Province of Trujillo, La libertad, Peru"

G = ox.graph_from_place(place_name, network_type="drive")

# show=False para que no se muestr ya que queremos guardarlo
ox.plot_graph(G, node_size=1,node_color="red",show=False,save=True,filepath="./img/mapa.png")


