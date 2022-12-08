import read_files


# E_matrix_barge = read_files.E[0]
# E_matrix_truck = read_files.E[82]

E_matrix_All = read_files.E_matrix_All
H_matrix = read_files.H_matrix

# Order of visited nodes
traject = []

def a_star(graph, heuristic, start, goal, traject):
    """
    Finds the shortest distance between two nodes using the A-star (A*) algorithm
    :param graph: an adjacency-matrix-representation of the graph where (x,y) is the weight of the edge or 0 if there is no edge.
    :param heuristic: an estimation of distance from node x to y that is guaranteed to be lower than the actual distance. E.g. straight-line distance
    :param start: the node to start from.
    :param goal: the node we're searching for
    :return: The shortest distance to the goal node. Can be easily modified to return the path.
    """

    # This contains the distances from the start node to all other nodes, initialized with a distance of "Infinity"
    distances = [float("inf")] * len(graph)

    # The distance from the start node to itself is of course 0
    distances[start] = 0

    # This contains the priorities with which to visit the nodes, calculated using the heuristic.
    priorities = [float("inf")] * len(graph)

    # start node has a priority equal to straight line distance to goal. It will be the first to be expanded.
    priorities[start] = heuristic[start][goal]

    # This contains whether a node was already visited
    visited = [False] * len(graph)

    # While there are nodes left to visit...
    while True:
        # ... find the node with the currently lowest priority...
        lowest_priority = float("inf")
        lowest_priority_index = -1
        for i in range(len(priorities)):
            # ... by going through all nodes that haven't been visited yet
            if priorities[i] < lowest_priority and not visited[i]:
                lowest_priority = priorities[i]
                lowest_priority_index = i

        if lowest_priority_index == -1:
            # There was no node not yet visited --> Node not found
            return -1

        elif lowest_priority_index == goal:
            # Goal node found
            traject.append(lowest_priority_index)
            print("Visiting node " + f"{lowest_priority_index}" + " with currently lowest priority of " + f"{lowest_priority}")
            print("Goal node found!")
            return distances[lowest_priority_index]

        traject.append(lowest_priority_index)
        print("Visiting node " + f"{lowest_priority_index}" + " with currently lowest priority of " + f"{lowest_priority}")


        # ...then, for all neighboring nodes that haven't been visited yet....
        for i in range(len(graph[lowest_priority_index])):
            if graph[lowest_priority_index][i] != 0 and not visited[i]:
                # ...if the path over this edge is shorter...
                if distances[lowest_priority_index] + graph[lowest_priority_index][i] < distances[i]:
                    # ...save this path as new shortest path
                    distances[i] = distances[lowest_priority_index] + graph[lowest_priority_index][i]
                    # ...and set the priority with which we should continue with this node
                    priorities[i] = distances[i] + heuristic[i][goal]
                    # print("Updating distance of node " + f"\n{i}" + " to " + f"\n{distances[i]}" + " and priority to " + f"\n{priorities[i]}")

                # Lastly, note that we are finished with this node.
                visited[lowest_priority_index] = True
                # print("Visited nodes: " + f"\n{visited}")
                # print("Currently lowest distances: " + f"\n{distances}")


a_star(graph= E_matrix_All,
       heuristic= H_matrix,
       start= 4,
       goal= 7,
       traject= traject)

