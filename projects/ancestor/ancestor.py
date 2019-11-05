from graph import Graph
def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = Graph()
    for i in ancestors:
        if i[0] not in ancestor_graph.vertices:
            ancestor_graph.add_vertex(i[0])
        if i[1] not in ancestor_graph.vertices:
            ancestor_graph.add_vertex(i[1])
        # print("------>", ancestor_graph.vertices)
    for i in ancestors:
        ancestor_graph.add_edge(i[0], i[1])

    print("------>", ancestor_graph.vertices)
        
