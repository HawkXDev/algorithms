graph = {
    "a": {
        "fin": 1
    },
    "b": {
        "a": 3,
        "fin": 5
    },
    "fin": {}  # The end node has no neighbors
}

infinity = float("inf")
costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

parents = {
    "a": "start",
    "b": "start"
}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:  # Iterate through all nodes
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            # If it is the node with the lowest cost already seen, and it has not yet been processed,
            lowest_cost = cost  # it is assigned to the new node with the lowest cost
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs)  # Find the node with the lowest cost among the raw

while node is not None:  # If all nodes are processed, the while loop is completed
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():  # Iterate through all the neighbors of the current node
        new_cost = cost + neighbors[n]

        if costs[n] > new_cost:  # If a neighbor can be reached faster through the current node,
            costs[n] = new_cost  # update the cost for this node
            parents[n] = node  # This node becomes the new parent for the neighbor

    processed.append(node)  # The node is marked as processed
    node = find_lowest_cost_node(costs)  # Find the next node to process and repeat the cycle

print('<parents> {')
for k, v in parents.items():
    print(f'\t{k}: {v}')
print('}')
