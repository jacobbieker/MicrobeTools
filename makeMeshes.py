from skimage import measure
import skvideo.io
import numpy as np
import os
import click


@click.command()
@click.argument('mask', type=click.Path(exists=True, dir_okay=False))
@click.argument('step_size', type=int)
@click.argument('spacing', type=list)
@click.argument('output', type=str, default="mask.obj")
@click.option('-v', '--video', help='Make mask from video input', is_flag=True)
@click.option('-m', '--multiple', help='Multiple masks in input', is_flag=True)
def make_mesh(mask, step_size, spacing, output, video, multiple):
    if video:
        # Need to convert video to 3D mask
        mask = skvideo.io.vread(mask)[:, :, :, 0]
        print(mask.shape)
    else:
        mask = np.load(mask)
        print(mask.shape)

    verts, faces, normals, values = measure.marching_cubes_lewiner(mask, spacing=(6.,1.,1.), step_size=step_size)
    print("Verticies: " + str(len(verts)))

    thefile = open(output, 'w')
    for item in verts:
        thefile.write("v {0} {1} {2}\n".format(item[0], item[1], item[2]))

    for item in normals:
        thefile.write("vn {0} {1} {2}\n".format(item[0], item[1], item[2]))

    for item in faces:
        thefile.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(item[0], item[1], item[2]))

    thefile.close()


if __name__ == "__main__":
    make_mesh()
