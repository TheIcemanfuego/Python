# -*- coding: utf-8 -*-

#Def 1
# A Graph is an ordered triple (V(G), E(G), Phi(G))
# where:
# V(G) is the set of all vertices in G
# E(G) is the set of all edges
# Phi_G() is an incidence function mapping a given edge to a pair of adjacent vertices

from enum import Enum

class State(Enum) :
    UNDEFINED = -1
    FALSE     = 0
    TRUE      = 1
    


class Graph():
    
    def __init__(self, name):
        self.graphID = hex(id(self))
        self.name    = None
        self.edgeMap     = {}
        self.edges       = []
        self.vertexMap   = {}
        self.vertices    = []
        
        
        # Graph properties
        self.hasLoop  = State.UNDEFINED
        self.isPlanar = State.UNDEFINED
        self.isSimple = State.UNDEFINED
        self.cntVertex = State.UNDEFINED
        self.cntEdge   = State.UNDEFINED
        
        try:
            assert isinstance(name, str)
        except AssertionError as err:
            raise TypeError("name is not an instance of the object str!", err.args)
        except Exception as exception:
            raise Exception("There was an undefined Exception!", exception.args)
        finally:
            pass
        
        self.name = name
        
    def __connect__(self, vertex1, vertex2):
        try:
            assert isinstance(vertex1, Vertex)
            assert isinstance(vertex2, Vertex)
        except TypeError as err:
            raise TypeError("One of the arguments is not an Instance of Object Vertex!: ", err.args)
        
        try:                        
            assert self.graphID == vertex1.graphID
            assert self.graphID == vertex2.graphID            
            
        except AssertionError as err:
            raise AssertionError("vertex belongs to a different graph!", err.args)
        except Exception as exception:
            raise Exception("There was an undefined Exception!", exception.args)
        finally:
            pass
        
        Edge(self, vertex1, vertex2)

        
    def __add__(self, vertex):
        try:
            assert isinstance(vertex, Vertex)
        except AssertionError as err:
            raise TypeError("vertex is not an instance of the object Vertex!", err.args)
        except Exception as exception:
           raise Exception("There was an undefined Exception!", exception.args) 
        finally:
            pass
        
        Vertex(self, vertex)
        
    def setGraphProperties(self):
        pass
    
    def __str__(self):
        return "Graph {0} located at {1}: ".format(self.name, self.graphID)
    
    def __report__(self):
        
        print(self)
        print("Vertices: "+str(self.vertexMap.keys()))
        print("Edges: "+str(self.edgeMap.keys())+"\n")

#        print("Vertices:")
#        print("-----------------------")
#        for v in self.vertices:
#            print(v)

        print("Incidence:")
        print("-----------------------")
        for e in self.edges:
            print(e)

    def incidence(self, edge):
        try:
            assert isinstance(edge, Edge)
            #assert isinstance(vertex2, Vertex)
        except TypeError as err:
            raise TypeError("edge is not an Instance of Object Edge!: ", err.args)
        finally:
            pass
        
        return edge.incidence

        
class Vertex():
    
    def __init__(self, graph):
        
        try:
            assert isinstance(graph, Graph)
        except AssertionError as err:
            raise AssertionError("graph is not an instance of the Graph object: ", err.args)
        except Exception as exception:
            raise Exception("There was an undefined Exception!", exception.args)
        finally:
            pass
            
        self.graphID = graph.graphID
        self.vertexID = hex(id(self))
        self.name = None
        
        vertex_index = len(graph.vertexMap) + 1
        self.name = "v"+str(vertex_index)
        graph.vertexMap.update({self.name : self.vertexID})
        graph.vertices.append(self)
    

    def __str__(self):
        return "Vertex {0} located at {1}\n".format(self.name, self.vertexID)



class Edge(set):
    
    def __init__(self, graph, vertex1, vertex2):
        try:
            assert isinstance(graph, Graph)
        except AssertionError as err:
            raise AssertionError("graph is not an instance of the Graph object: ", err.args)
        except Exception as exception:
            raise Exception("There was an undefined Exception!", exception.args)
        finally:
            pass
        
        self.edgeID  = hex(id(self))
        self.graphID = graph.graphID
        self.name    = None
        self.vertices = None
        
        edge_index = len(graph.edgeMap) + 1
        self.name  = "e"+str(edge_index)
        self.incidence = (vertex1.name, vertex2.name)
        graph.edgeMap.update({self.name : (vertex1.vertexID, vertex2.vertexID)})
        
        if (vertex1.vertexID == vertex2.vertexID):
            graph.hasLoop = True
            
        graph.edges.append(self)
        
        
    def __str__(self):
        return "Edge {0} connects vertices {1} and {2}.".format(self.name, self.incidence[0], self.incidence[1])

if __name__ == "__main__":
    
    g = Graph('G1')

# Interaction method 1
# Explicit instantiation and explicit creation of incidence function
# via variable referencing.
#    v1 = Vertex(g)
#    v2 = Vertex(g)
#    v3 = Vertex(g)
#    v4 = Vertex(g)
#    v5 = Vertex(g)
    
    
#    g.__connect__(v1,v2)
#    g.__connect__(v2,v3)
#    g.__connect__(v3,v3)
#    g.__connect__(v3,v4)
#    g.__connect__(v2,v4)
#    g.__connect__(v4,v5)
#    g.__connect__(v2,v5)
#    g.__connect__(v2,v5)


# Interaction method 2
# Implicit instantiation of vertices and explicit creation of
# incidence functions via explicit indexing.
    Vertex(g)
    Vertex(g)
    Vertex(g)
    Vertex(g)
    Vertex(g)    

    g.__connect__(g.vertices[0], g.vertices[1])
    g.__connect__(g.vertices[1], g.vertices[2])
    g.__connect__(g.vertices[2], g.vertices[2])
    g.__connect__(g.vertices[2], g.vertices[3])
    g.__connect__(g.vertices[1], g.vertices[3])
    g.__connect__(g.vertices[3], g.vertices[4])
    g.__connect__(g.vertices[1], g.vertices[4])
    g.__connect__(g.vertices[1], g.vertices[4])
    
    g.__report__()