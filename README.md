# MicrobeTools
Various scripts to convert data to work with the MicrobeVisualization Software

# Installation

1. ```git clone https://github.com/jacobbieker/MicrobeTools.git```
2. ```cd``` into the directory
3. ```pip install -r requirements```
4. Use it! 

# Instructions

The use of the scripts is fairly easy. The most important one is the makeMeshes.py. This script takes as input the path to either a Numpy mask or video file containing the masked images. 

The input has to be formatted like this:

``` [INPUT FILE PATH] [STEP SIZE FOR MARCHING CUBE] [RELATIVE SIZE OF DIMENSIONS] [OUTPUT NAME (OPTIONAL, defaults to 'mask.obj')] [-v or --video if input is video] ```

where ```STEP SIZE``` is an Integer, ```SIZE OF DIMENSIONS``` is a tuple of three floats in (Z,X,Y) format, i.e. (6.,1.,1.) for example.

The script will then run, creating a ```.obj``` file that can then be loaded into a variety of visualization software, including Meshlab, and the MicrobeVisualization VR software. The script also outputs the number of verticies in the output mask, and the overall size of the cube of data to help make sure it is handling it correctly. 

# Examples

Say you have a mask saved in npx format with the name ```intestinal_outline```. The spacing of the z axis relative to the x and y is 6:1, and you want a  step size of 1 for the marching cubes, and a final file named gut_outline.obj. The command would then be:

```python makeMeshes.py intestinal_outline.npz 1 [6.,1.,1.] gut_outline.obj```

# Notes

When using a small step size, the number of verticies can quickly explode. It is recommended to use a larger step size (~5) in the beginning as a quick check to make sure the mask looks reoughly correct.

Objects with large numbers of verticies (above 64335) should not be loaded directly into the VR system, as the performance suffers greatly and can freeze or be very sluggish. For large meshes, Meshlab is the recommended software to laod the mesh into. 
