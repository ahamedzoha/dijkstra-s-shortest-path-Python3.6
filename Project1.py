def dijkstra(graph, source, distance, parent):
    #print("inside function")
    unvisited_set = [i for i in range(len(distance))]

    distance[source] = 0

    while unvisited_set:
        #print("inside 1st loop")
        u = minDist(unvisited_set,distance)
        #print(u)
        unvisited_set.remove(u)

        for n in range(len(graph[u])):
            if graph[u][n] != -1:
                dis = distance[u] + graph[u][n]
                if dis < distance[n]:
                    distance[n] = dis
                    parent[n] = u
    
def minDist(Q, dis):
    min = Q[0]
    for v in Q:
        if dis[v] < dis[min]:
            min = v
    
    return min

num_nodes = int(input("number of nodes: "))
connectivity = float(input("Percentage of connectivity(1-100): "))

node_set = [[0 for x in range(num_nodes)] for y in range(num_nodes)]

distance_set = [10000000 for x in range(num_nodes)]
parent_set = [-1 for x in range(num_nodes)]

for i in range(num_nodes):
    for j in range(i):
        weight = int(input("weight of {x},{y}: ".format(x=i, y=j)))
        node_set[i][j] = weight
        node_set[j][i] = weight

for line in node_set:
    print(line)

dijkstra(node_set, 1, distance_set, parent_set)

t = int(input("target: "))
s = str(t)
while parent_set[t] != -1:
    s = str(parent_set[t]) +"->" +s
    t = parent_set[t]
print(distance_set)
print(s)

'''
class Node(object):
    """Node objects to store information about a particular node's: weight, through, visited"""

    weight = -1
    through = -1
    visited = False

    def __init__(self, weight = -1, throu6gh = -1, visited = False):
        self.weight = int(weight)
        self.through = int(through)
        self.visited = bool(visited)



#print("Number of nodes: ", unvisited_set)
#print(unvisited_set[1])
#print("Connectivity percentage: ", connectivity)
#print(uplist[:],"\n")
'''