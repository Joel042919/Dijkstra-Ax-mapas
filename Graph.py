class Directed_Graph:
    def __init__(self):
        self.graph_dict={}
         
    def add_vertex(self,vertex):
        if vertex in self.graph_dict:
            return "Vertex Already in graph"
        self.graph_dict[vertex]=[]
    
    def add_edge(self,edge):
        v1=edge.get_v1()
        v2=edge.get_v2()
        weight = edge.get_weight()
        if v1 not in self.graph_dict:
            raise ValueError(f'Vertex {v1.get_name()} not in graph')
        if v2 not in self.graph_dict:
            raise ValueError(f'Vertex {v2.get_name()} not in graph')
        self.graph_dict[v1].append([v2,weight])
    
    def is_vertex_in(self,vertex):
        return vertex in self.graph_dict

    def get_vertex(self,vertex_name):
        """
        find_vertex=list(filter(lambda v:v.get_name()==vertex_name,self.graph_dict))
        return find_vertex[0] if find_vertex[0]==None else f'Vertex {vertex_name} does not exist'"""
        for v in self.graph_dict:
            if vertex_name == v.get_name():return v
        print(f'Vertex {vertex_name} does not exist')
    
    def get_neighbours(self, vertex):
        return self.graph_dict[vertex]
    
    def __str__(self):
        all_edges = ''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges +=v1.get_name() + f' ---{v2[1]}---> ' + v2[0].get_name() + '\n'
        return all_edges
        
        
        
class Edge:
    def __init__(self,v1,v2,weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
    def get_v1(self):
        return self.v1
    def get_v2(self):
        return self.v2
    def get_weight(self):
        return self.weight
    def __str__(self):
        return self.v1.get_name() + f' ---{self.get_weight()}---> ' + self.v2.get_name()
    
class Vertex:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name
 
class Undirected_Graph(Directed_Graph):
    def add_edge(self, edge):
        Directed_Graph.add_edge(self, edge)
        edge_back = Edge(edge.get_v2(), edge.get_v1(),edge.get_weight())
        Directed_Graph.add_edge(self, edge_back)
       


def build_graph(graph):
    g = graph()
    for v in ('s','a','b','c','d','e','f','g','i','x'):
        g.add_vertex(Vertex(v))
    
    g.add_edge(Edge(g.get_vertex('a'),g.get_vertex('b'),4))
    g.add_edge(Edge(g.get_vertex('a'),g.get_vertex('f'),10))
    g.add_edge(Edge(g.get_vertex('a'),g.get_vertex('i'),9))
    
    g.add_edge(Edge(g.get_vertex('s'),g.get_vertex('b'),5))
    g.add_edge(Edge(g.get_vertex('s'),g.get_vertex('c'),3))
    
    g.add_edge(Edge(g.get_vertex('x'),g.get_vertex('c'),10))
    g.add_edge(Edge(g.get_vertex('x'),g.get_vertex('f'),3))
    g.add_edge(Edge(g.get_vertex('x'),g.get_vertex('b'),1))
    
    g.add_edge(Edge(g.get_vertex('f'),g.get_vertex('g'),6))
    
    g.add_edge(Edge(g.get_vertex('g'),g.get_vertex('e'),7))
    
    g.add_edge(Edge(g.get_vertex('e'),g.get_vertex('d'),3))
    g.add_edge(Edge(g.get_vertex('d'),g.get_vertex('c'),6))
    g.add_edge(Edge(g.get_vertex('e'),g.get_vertex('c'),9))

    return g
    

G1 = build_graph(Undirected_Graph)

print(G1)