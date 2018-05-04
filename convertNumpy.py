import numpy as np


data1 = np.load("intestinal_outline.npz")
print(data1.files)
data2 = data1['images']
non_zeros = np.transpose(np.nonzero(data2))

data = np.load("rough_mask.npy")
non_zeros1 = np.transpose(np.nonzero(data))
print(non_zeros)

timeseries = np.load("gut_outline_DIC.npz")
print(timeseries.files)
timeseries_data = timeseries['images']
time_non_zeros = np.transpose(np.nonzero(timeseries_data))

"""
Now do the gut outline
"""

with open("gut_timeseries.csv", "w") as outfile:
    outfile.write("ClusterNumber,X,Y,Z\n")
    new_data = []
    mesh_counter = 0
    for element in non_zeros1:
        outfile.write("{},{},{},{}\n".format(np.int(np.ceil(mesh_counter/64000)), element[0], element[1], element[2]))
        mesh_counter += 1

with open("gut2.csv", "w") as outfile:
    outfile.write("ClusterNumber,X,Y,Z\n")
    new_data = []
    mesh_counter = 0
    for element in non_zeros1:
        outfile.write("{},{},{},{}\n".format(np.int(np.ceil(mesh_counter/64000)), element[0], element[1], element[2]))
        mesh_counter += 1

with open("gut2.csv", "w") as outfile:
    outfile.write("ClusterNumber,X,Y,Z\n")
    new_data = []
    for element in non_zeros:
        new_data.append([data[element[0]][element[1]][element[2]], element[0], element[1], element[2]])

    s = sorted(new_data, key = lambda x: (x[0], x[1], x[2], x[3]))

    #now have the non-zeros, need to prune those that are not in the edges:
    temp_array = []
    temp_above = None
    temp_clusterNum = None
    temp_z_val_above = None
    temp_z_val_below = None
    temp_below = None
    temp_clusterNum_below = None
    temp_clusterNum_above = None
    # add the first two, since otherwise they will be skipped
    temp_array.append(new_data[0])
    temp_array.append(new_data[1])
    for index, element in enumerate(new_data):
        if index < 2:
            continue
        if new_data[index - 2][0] == element[0] == new_data[index - 1][0]:
            # all in same cluster, and if None, still fials check below
            # Both are set, so go ahead and check
            if new_data[index - 2][1] == new_data[index -1][1] and element[1] == new_data[index - 1][1]:
                # now checking if the same z, so same slice
                # since its the same, can remove this point if either x or y are the same for the three
                # Now check if Y is same:
                if new_data[index - 2][2] == new_data[index -1][2] and new_data[index][2] == new_data[index - 1][2]:
                    print("Continuing\n")
                    continue
                    # These ones match, so don't add it to the new array
                else:
                    # Add to array
                    temp_array.append(new_data[index - 1])
            else:
                temp_array.append(new_data[index - 1])
        else:
            # Element does not match previous ones, so add
            temp_array.append(new_data[index - 1])


            # Cluster number, or something else, does not match

    temp_array = sorted(temp_array, key = lambda x: (x[0], x[1], x[2], x[3]))
    mesh_counter = 0
    for element in temp_array:
        outfile.write("{},{},{},{}\n".format(np.int(np.ceil(mesh_counter/64000)), element[0], element[1], element[2]))
        mesh_counter += 1
