class Graph():
    def __init__(self):
        self.vertex = {}
    
    def add_edge(self,src,dest): # undirectged graph

        if src<0 or dest <0:
            print('Invalid Edge')
            return
        
        # for src to dest
        if  src in self.vertex:
            if dest not in self.vertex[src]:
                self.vertex[src].append(dest)
        else:
            self.vertex[src] = []
            self.vertex[src].append(dest)
        
        # for dest to src
        if dest in self.vertex:
            if src not in  self.vertex[dest]:
                self.vertex[dest].append(src)
                
        else:
            self.vertex[dest] = []
            self.vertex[dest].append(src)

    def print_matrix(self):
        for v in self.vertex:
            print(f'{v} --> {self.vertex[v]}')
        
g = Graph()
g.print_matrix()
g.add_edge(1,2)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(3,1)
g.add_edge(0,0)
g.print_matrix()