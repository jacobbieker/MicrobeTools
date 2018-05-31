from skimage import measure

import numpy as np
import os

@click.command()
@click.argument('mask', type=click.Path(exists=True, dir_okay=False), help='Input Mask or video file')
@click.argument('step_size', type=int, help='Step size for the Marching Cubes, higher values give lower resolution')
@click.argument('spacing', type=tuple, help='Spacing of the slices in (Z,X,Y) format, defaults to (6,1,1)')
@click.argument('-o', '--output', type=str, help='Output name for the OBJ file')
@click.option('-v', '--video', help='Make mask from video input', is_flag=True)
def make_mesh(mask, step_size, spacing, output, yes, video):
    verts, faces, normals, values = measure.marching_cubes_lewiner(mask, spacing=spacing, step_size=step_size)
    print("Verticies: " + str(len(verts)))

    thefile = open(output, 'w')
    for item in verts:
        thefile.write("v {0} {1} {2}\n".format(item[0],item[1],item[2]))

    for item in normals:
        thefile.write("vn {0} {1} {2}\n".format(item[0],item[1],item[2]))

    for item in faces:
        thefile.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(item[0],item[1],item[2]))

    thefile.close()
