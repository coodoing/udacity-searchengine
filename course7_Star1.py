def reachable(graph, node):
    reachable_nodes = []    
    nodes_to_travel = graph[node]
    #print(nodes_to_travel)
    while nodes_to_travel:
        current_node = nodes_to_travel.pop()
        #print(current_node)
        if current_node not in reachable_nodes:
            #print(graph[current_node])
            #if graph[current_node] not in nodes_to_travel:
            nodes_to_travel.extend(graph[current_node])
                #print(nodes_to_travel)
            reachable_nodes.append(current_node)

    if node not in reachable_nodes:
        reachable_nodes.extend(node)
    return reachable_nodes


graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}

#print (reachable(graph, 'a'))
#>>> ['a', 'c', 'd', 'b']

#print (reachable(graph, 'd'))
#>>> ['d', 'a', 'c', 'b']

print(reachable(graph, 'e'))
#>>> ['e', 'a', 'c', 'd', 'b']
