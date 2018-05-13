import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from skimage import measure
from skimage.draw import ellipsoid

import numpy as np


#data2 = np.load("gut_outline_DIC.npz")['images']
data2 = np.load("intestinal_outline.npz")['images']


#data2 = np.load("rough_mask.npy")

#zeroes = np.zeros(data2.shape)

#for x in range(data2.shape[0]):
#    for y in range(data2.shape[1]):
#        for z in range(data2.shape[2]):
#            if data2[x][y][z] == 2:
#                zeroes[x][y][z] = 1

# Now have a thing with only the ones



#print(data1.files)
#data2 = data1['images']
#non_zeros = np.transpose(np.nonzero(data2))
# Display resulting triangular mesh using Matplotlib. This can also be done

verts, faces, normals, values = measure.marching_cubes_lewiner(data2, spacing=(9,6,6))
print("Verticies: " + str(len(verts)))

#verts, faces, normals, values = measure.marching_cubes_lewiner(data1, 0)

faces= faces+1

thefile = open('fixed_gut_5.obj', 'w')
for item in verts:
    thefile.write("v {0} {1} {2}\n".format(item[0],item[1],item[2]))

for item in normals:
    thefile.write("vn {0} {1} {2}\n".format(item[0],item[1],item[2]))

for item in faces:
    thefile.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(item[0],item[1],item[2]))

thefile.close()
