from queue import PriorityQueue
import math

# A priority queue is a container data structure that manages a set of records with totally-ordered keys to provide quick access to the record with the smallest or largest key in the set.
# It retrieves the highest-priority element. 
# The priority of individual elements is decided by the ordering applied to their keys.

def shortest_path(M, start, goal):
    pathQueue = PriorityQueue()
    pathQueue.put(start, 0)
    
    previous = {start: None}
    cost = {start: 0}
    
    while not pathQueue.empty():
        current = pathQueue.get()
        # print(current)
        if current == goal:
            generate_path(previous, start, goal)
           
        # M.roads[current] <- intersections connected to given intersection
        for node in M.roads[current]:
            update_cost = cost[current] + distance_between(M.intersections[current], M.intersections[node])

            # if point (node) has not been visited or the new cost is lower than the previous
            # update total_cost and add to Queue
            if node not in cost or update_cost < cost[node]:
                cost[node] = update_cost
                total_cost = update_cost + distance_between(M.intersections[current], M.intersections[node])
                pathQueue.put(node, total_cost)
                previous[node] = current

    return generate_path(previous, start, goal)


# find the distance between two points on the map (as the crow flies)
def distance_between(a, b):
    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))
    
    
# generate a reversed path list from start point to goal
def generate_path(previous, start, goal):
    current = goal
    path_list = [current]
    while current != start:
        current = previous[current]
        path_list.append(current)
    # print(path_list)
    path_list.reverse()
    return path_list


# Resource: https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode