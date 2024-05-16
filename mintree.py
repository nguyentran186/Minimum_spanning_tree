import numpy as np

or_list = []

with open('input.txt', 'r') as file:
    for line in file:
        or_list.append(list(map(int, line.strip().split())))

unique_values = set()

# Iterate over each sublist in or_list
for sublist in or_list:
    # Extract values from the specified indices [0:2] (inclusive)
    unique_values.update(sublist[0:2])

# Convert the set to a sorted list if needed
point_num = len(unique_values)


def minWeight(list):
    weight = []
    for x in list:
        weight.append(x[2])
    return np.argmin(weight)

point_list = []
edge_list = []

# Process 1st edge
first_idx = minWeight(or_list)

# Add first edge to edge list
edge_list.append(or_list[first_idx])

first_point = or_list[first_idx]

# Add first 2 points to point list
point_list.append(first_point[0])
point_list.append(first_point[1])
print("Initial point list: ", first_point[0], ", ", first_point[1])
print("Initial edge: ", or_list[first_idx])

possible_out = []
or_list.remove(first_point)
for edge in or_list:
    if edge[0] in first_point[0:2] or edge[1] in first_point[0:2]:
        possible_out.append(edge)

# Process next n-2 edge
for i in range(0, point_num-2):
    #Find min weight
    min_idx = minWeight(possible_out)
    
    #Append to edge list
    edge_list.append(possible_out[min_idx])
    
    #Remove new edge in possible_out
    new_edge = possible_out[min_idx]
    or_list.remove(new_edge)
    possible_out.remove(new_edge)
    new_point = new_edge[0] if new_edge[1] in point_list else new_edge[1]
    
    
    #Append new point to point list
    point_list.append(new_point)
    print("New point add to tree: ", new_point, "\tNew edge connect: ", new_edge, "\tPossible edge connect next", possible_out)
    length = len(possible_out)
    
    #Remove old edge due to new edge in possible out
    i = 0
    while (i < length):
        remove_edge = possible_out[i]
        if remove_edge[0] == new_point or remove_edge[1] == new_point:
            i = i-1
            length = length - 1
            possible_out.remove(remove_edge)
        i = i + 1
    
    #Append new edge to possible out        
    for edge in or_list:
        if (edge[0] == new_point and edge[1] not in point_list) or (edge[1] == new_point and edge[0] not in point_list):
            possible_out.append(edge)

# Print result   
print(edge_list)

    