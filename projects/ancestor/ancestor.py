from graph import Graph
def earliest_ancestor(ancestors, starting_node):
    # Create a new graph for the ancestors
    ancestor_graph = Graph()
    # early_ancestors = {}
    # Add all vertices
    for i in ancestors:
        if i[0] not in ancestor_graph.vertices:
            ancestor_graph.add_vertex(i[0])
        if i[1] not in ancestor_graph.vertices:
            ancestor_graph.add_vertex(i[1])
    # Add edges
    for i in ancestors:
        ancestor_graph.add_edge(i[1], i[0])

    if not ancestor_graph.vertices[starting_node]:
        print("return from no children of starting_node: ", -1)
        return -1
    # print("------>", ancestor_graph.vertices)
    print("return from earliest_ancestor: ", ancestor_graph.dfs_deepest(starting_node))
    return ancestor_graph.dfs_deepest(starting_node)
        
