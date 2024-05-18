import osmnx as ox
import heapq
import random

import tempfile


"""IMPORTING AND CLEANING THE MAP"""

place_name = "Trujillo, Province of Trujillo, La libertad, Peru"

G = ox.graph_from_place(place_name, network_type="drive")

# Save the images of the mapa get by openstreetmap
ox.plot_graph(G, node_size=1,node_color="red",show=False,save=True,filepath="./img/mapa.png")

for edge in G.edges:
    #Cleaning the "maxspeed" attribute (some are lists, strings or none)
    maxspeed = 40
    if "maxspeed" in G.edges[edge]:
        maxspeed = G.edges[edge]["maxspeed"]
        if type(maxspeed) ==list:
            speeds = [int(speed[0:2]) for speed in maxspeed]
            print(speeds)
            maxspeed = min(speeds)
        elif type(maxspeed) == str:
            maxspeed = int(maxspeed[0:2])
    G.edges[edge]["maxspeed"]=maxspeed       
    #Adding the weight attribute (time=distance/speed)
    G.edges[edge]["weight"] = G.edges[edge]["length"]/maxspeed
    


"""VISUAL UTILS"""

def style_unvisited_edge(edge):
    G.edges[edge]["color"]="#d36206"
    G.edges[edge]["alpha"]=1
    G.edges[edge]["linewidth"]=1
    
def style_visited_edge(edge):
    G.edges[edge]["color"]="#d36206"
    G.edges[edge]["alpha"]=1
    G.edges[edge]["linewidth"]=1
    
def style_active_edge(edge):
    G.edges[edge]["color"]="white"
    G.edges[edge]["alpha"]=1
    G.edges[edge]["linewidth"]=1
    
def style_path_edge(edge):
    G.edges[edge]["color"]="white"
    G.edges[edge]["alpha"]=1
    G.edges[edge]["linewidth"]=1
    

## Mostrar con interfaz gráfica
def plot_graph():
    ox.plot_graph(
        G,
        node_size=[G.nodes[node]["size"] for node in G.nodes],
        edge_color = [G.edges[edge]["color"] for edge in G.edges],
        edge_alpha = [ G.edges[edge]["alpha"] for edge in G.edges],
        edge_linewidth = [G.edges[edge]["linewidth"] for edge in G.edges],
        node_color = "white",
        bgcolor= "#18080e"
    )
    
    
## Mostrar sin interfaz gráfica
def plot_graph_sin():
    temp_file = "./img/ruta.png"
    ox.plot_graph(
        G,
        node_size=[G.nodes[node]["size"] for node in G.nodes],
        edge_color=[G.edges[edge]["color"] for edge in G.edges],
        edge_alpha=[G.edges[edge]["alpha"] for edge in G.edges],
        edge_linewidth=[G.edges[edge]["linewidth"] for edge in G.edges],
        node_color="white",
        bgcolor="#18080e",
        save=True,
        filepath=temp_file
    )
    print(f"Graph saved to {temp_file}")



"""ALGORITHMS IMPLEMENTATION"""

def dijkstra(orig,dest,plot=False):
    for node in G.nodes:
        G.nodes[node]["visited"]=False
        G.nodes[node]["distance"]=float("inf")
        G.nodes[node]["previous"]=None
        G.nodes[node]["size"]=0
        
    for edge in G.edges:
        style_unvisited_edge(edge)
    
    G.nodes[orig]["distance"]=0
    G.nodes[orig]["size"]=50
    G.nodes[dest]["size"]=50
    pq=[(0,orig)]
    step = 0
    while pq:
        _,node = heapq.heappop(pq)
        if node == dest:
            if plot:
                print("Iteraciones:",step)
                plot_graph_sin()
            return
        if G.nodes[node]["visited"]: continue
        G.nodes[node]["visited"] = True
        for edge in G.out_edges(node):
            style_visited_edge((edge[0],edge[1],0))
            neighbor = edge[1]
            weight = G.edges[(edge[0],edge[1],0)]["weight"]
            if G.nodes[neighbor]["distance"]>G.nodes[node]["distance"]+weight:
                G.nodes[neighbor]["distance"]=G.nodes[node]["distance"]+weight
                G.nodes[neighbor]["previous"]=node
                heapq.heappush(pq,(G.nodes[neighbor]["distance"],neighbor))
                for edge2 in G.out_edges(neighbor):
                    style_active_edge((edge2[0],edge2[1],0))
        step+=1

   ##A* distancia euclidian
def distance(node1, node2):
    x1,y1 = G.nodes[node1]["x"],G.nodes[node1]["y"]
    x2,y2 = G.nodes[node2]["x"],G.nodes[node2]["y"]
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def a_star(orig,dest,plot=False):
    for node in G.nodes:
        G.nodes[node]["previous"]=None
        G.nodes[node]["size"]=0
        G.nodes[node]["g_score"]=float("inf")
        G.nodes[node]["f_score"]=float("inf")
    for edge in G.edges:
        style_unvisited_edge(edge)
    G.nodes[orig]["size"]=50
    G.nodes[dest]["size"]=50
    G.nodes[orig]["g_score"]=0
    G.nodes[orig]["f_score"]=distance(orig,dest)
    pq=[(G.nodes[orig]["f_score"],orig)]
    step=0
    while pq:
        _,node = heapq.heappop(pq)
        if node==dest:
            if plot:
                print("Iteraciones:",step)
                plot_graph_sin()
            return
        for edge in G.out_edges(node):
            style_active_edge((edge[0],edge[1],0))
            neighbor = edge[1]
            tentative_g_score = G.nodes[node]["g_score"]+distance(node,neighbor)
            if tentative_g_score<G.nodes[neighbor]["g_score"]:
                G.nodes[neighbor]["previous"]=node
                G.nodes[neighbor]["g_score"]=tentative_g_score
                G.nodes[neighbor]["f_score"]=tentative_g_score+distance(neighbor,dest) 
                heapq.heappush(pq,(G.nodes[neighbor]["f_score"],neighbor))  
                for edge2 in G.out_edges(neighbor):
                    style_active_edge((edge2[0],edge2[1],0))
        step+=1

def reconstruct_path(orig,dest,plot=False,algorithm=None):
    for edge in G.edges:
        style_unvisited_edge(edge)
    dist=0
    speeds=[]
    curr = dest
    while curr!=orig:
        prev = G.nodes[curr]["previous"]
        dist+=G.edges[(prev,curr,0)]["length"] 
        speeds.append(G.edges[(prev,curr,0)]["maxspeed"])
        style_path_edge((prev,curr,0))
        if algorithm:
            G.edges[(prev,curr,0)][f"{algorithm}_uses"]=G.edges[(prev,curr,0)].get(f"{algorithm}_uses",0)+1
        curr=prev
    dist/=1000
    if plot:
        print(f"Distance: {dist}")
        print(f"Avg. speed: {sum(speeds)/len(speeds)}")
        print(f"Total time:{dist/(sum(speeds)/len(speeds))*60}")
        plot_graph_sin()
        


"""EJECUTAR COMO SCRIPT, NO COMO MODULO"""

if __name__=="__main__":    
    start = random.choice(list(G.nodes))
    end = random.choice(list(G.nodes))

    dijkstra(start,end,plot=True)
    reconstruct_path(start,end,plot=True)

    a_star(start,end,plot=True)
    reconstruct_path(start,end,plot=True)


