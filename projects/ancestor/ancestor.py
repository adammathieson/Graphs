# from graph import Graph
# def earliest_ancestor(ancestors, starting_node):
#     # Create a new graph for the ancestors
#     ancestor_graph = Graph()
#     # early_ancestors = {}
#     # Add all vertices
#     for i in ancestors:
#         if i[0] not in ancestor_graph.vertices:
#             ancestor_graph.add_vertex(i[0])
#         if i[1] not in ancestor_graph.vertices:
#             ancestor_graph.add_vertex(i[1])
#     # Add edges
#     for i in ancestors:
#         ancestor_graph.add_edge(i[1], i[0])

#     if not ancestor_graph.vertices[starting_node]:
#         print("return from no children of starting_node: ", -1)
#         return -1
#     # print("------>", ancestor_graph.vertices)
#     print("return from earliest_ancestor: ", ancestor_graph.dfs_deepest(starting_node))
#     return ancestor_graph.dfs_deepest(starting_node)

def earliest_ancestor(ancestors, starting_node):
    # start a queue and add starting node
    q = []
    q.append([starting_node])
    # initialize store of path
    store = [[starting_node]]
    # while queue is not empty
    while len(q) > 0:
        # dequeue first path and add the path to store of path ways
        path = q.pop(0)
        if len(path) > len(store[0]):
            store[0] = path
        # print(path, store)
        # grab last node from path
        last = path[-1]
        # loop through list of connections
        for tup in ancestors:
            # if the node is a child (i.e. second element of tuple)
            if last == tup[1]:
                # append the parent of the child to path and add to back of queue
                q.append(path + [tup[0]])
    # if len is only 1, we know the list only has original element and no parents
    if len(store[0]) == 1:
        return -1
    # else return last element of the result list
    else:
        return store[0][-1]
        
