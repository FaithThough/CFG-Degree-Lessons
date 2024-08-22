class Graph:
    def __init__(self, graph_dictionary=None):
        if graph_dictionary is None:
            graph_dictionary = {}
        self.graph_dictionary = graph_dictionary

    def get_vertices(self): # Get a list of all vertices in the graph, vertices are the keys of the graph dictionary
        return list(self.graph_dictionary.keys())

    def get_edges(self):
        edge_names = []
        for vertex in self.graph_dictionary:
            for next_vertex in self.graph_dictionary[vertex]: # Finding out the adjacent
                if {next_vertex, vertex} not in edge_names: # Ensures that they're not duplicated
                    edge_names.append({vertex, next_vertex})
        return edge_names

    def add_edge(self, edge):
        edge = set(edge) # In set we cannot have duplicate values
        (vertex1, vertex2) = tuple(edge)

        if vertex1 in self.graph_dictionary:
            self.graph_dictionary[vertex1].append(vertex2)
        else:
            self.graph_dictionary[vertex1] = [vertex2]

        if vertex2 in self.graph_dictionary:
            self.graph_dictionary[vertex2].append(vertex1)
        else:
            self.graph_dictionary[vertex2] = [vertex1]

graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}

g = Graph(graph_elements)

print(g.get_vertices())
print(g.add_edge(("e", "a")))
print(g.get_edges())









