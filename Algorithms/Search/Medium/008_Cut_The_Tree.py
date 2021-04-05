# https://www.hackerrank.com/challenges/cut-the-tree/problem

def cutTheTree(data, edges):
    # Constraints
    root_node = 1

    # Information about the data
    sum_data = sum(data)
    len_data = len(data)

    # Transform data into 1-based indexing
    data.insert(0, 0)

    # If one tree is very close to half the total value, the other one will also be
    optimal_sum_value = sum_data / 2

    # Store information about the tree
    connections = [[] for _ in range(len_data + 1)]  # All the connections
    tree_sums = [0 for _ in range(len_data + 1)]  # The sum of each sub-tree
    visited = [False for _ in range(len_data + 1)]  # All the visited nodes
    done = [False for _ in range(len_data + 1)]  # All the nodes with the correct sub-tree sum

    # Get all connections (two-ways)
    for e in edges:
        connections[e[0]] += [e[1]]
        connections[e[1]] += [e[0]]

    # Use a stack (iterative process to prevent Recursion Depth exception)
    stack = [root_node]
    while len(stack):
        # Get the parent node
        parent_node = stack[0]
        visited[parent_node] = True

        # Start counting the sum of all it's children
        children_sum = 0
        children_done = True

        # Analise the children
        for child in connections[parent_node]:
            # If the children hasn't been visited, remove the wrong way connection
            if not visited[child]:
                connections[child].remove(parent_node)

            # Add it's sub-tree value to the total
            children_sum += tree_sums[child]

            # If the children isn't done, we can't calculate the parent's sum
            if not done[child]:
                stack.insert(0, child)
                children_done = False

        # If all the children are done, then we know the parent's value
        if children_done:
            tree_sums[parent_node] = data[parent_node] + children_sum
            done[parent_node] = True
            stack.remove(parent_node)

    differences = []
    for t_s in tree_sums:
        differences += [abs(t_s - optimal_sum_value)]

    return int(min(differences) * 2)


data_test = [100, 200, 100, 500, 100, 600]
edges_test = [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]
print(cutTheTree(data_test, edges_test))
