# A graph is a non-linear data structure consisting of nodes (vertices) connected by edges. 
# It is used to model complex networks and relationships, where nodes represent entities (e.g., people, cities) and edges represent the connections between them 

# Directed Graph: goes only in one direction ex; we can go from 1-->2 but can not go 2-->1
#    eg; twiter network , a-->b a follow b but not necessary b follow a or b-->a

# Undirected Graph: we can go in both direction, ex; friend request

# Weighted Graph : assign a cost or value to an edge ex; distance in map

# Cyclic Graph: Cyclic graphs contain paths that loop back onto themselves

# simple code but more memory wastage

class Graph():

    def __init__(self,n): # n is number of vertex

        self.vertex = n
        self.m = [[0 for _ in range(n)] for _ in range(n)] 
    
    def add_edge(self,src,dest): # undirected 

        if src<0 or src>=self.vertex or dest<0 or dest>=self.vertex:
            print('Invalid Edge')
            return 
        
        self.m[src][dest] = 1
        self.m[dest][src] = 1
    
    def print(self):

        for row in self.m:
            print(' '.join(map(str,row)))

g = Graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,2)
g.add_edge(3,3)
g.print()
    
    