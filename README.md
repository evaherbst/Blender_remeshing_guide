# Blender Mesh Cleaning Guide 


For FEA (finite elemenet analysis) and also other goals such as animating or 3D printing, it is important to have clean meshes.
This guide offers step by step instructions to clean your meshes in the freeware Blender, which can be downloaded [here](https://www.blender.org/)

*This guide was created for Blender 2.9. Other versions might have slightly different settings*

**Aims of Mesh Cleaning**:
By cleaning a mesh, we want to make it watertight (e.g. no holes) and **manifold**. Manifold meshes mean that there are no problems such as faces with 0 area, edges connecting more than 2 faces, several vertices occupying the same position, etc. For finite element analysis, we also want to have the elements of the mesh be fairly uniform in size, and to avoid sharp triangles (angles of < 20 degrees and > 150 degrees). This practical guide will teach you how to create a mesh meeting all of these conditions.

___
*Before we get into the mesh cleaning, here are some useful Blender shortcuts and tips:*

### Useful Blender hotkeys:

- H Hide
- Alt + H Unhide all
- Shift + H Hide all except selected
- Alt + dragging MMB (middle mouse button) - switch between orthogonal views top, front, bottom, side, etc
- Edge loop select: hold alt, select edge with LMB
- In Edit mode, press 1,2,3 to switch between vertex, edge, and face selections
- Press tab to switch between object and edit modes
- For more hotkeys see this [list](https://techylawyer.com/blog/the-blender-2-8-keyboard-shortcuts-cheat-sheet-for-windows/) 
  - for Blender 2.8 but many hotkeys are still the same
- W to change selection mode (from box select to circle select to lasso select)
- F3 will pull up the search menu, so you can type in the same of any tool to search for it


### Some useful shortcuts/tools/settings:
- Tool option dialogue: Notice that sometimes the dialogue box for a tool won’t show up, or only after you apply the tool? You can fix this by pressing F9 to immediately see the mathematical options (for example if you want to rotate by 90 degrees about the X axis, you can type these values in the dialogue box).
- You can make your own shortcuts by right clicking on the operation in the menu, and clicking “assign shortcut”
- Tip: if you rename your object, your mesh will often still have the old mesh. (The  object is indicated by the orange upside down triangle in the hierarchy, and the mesh (indicated by the green upside down triangle). To set the name of all meshes to be the same as the object, go to scripting mode and paste the following Python script in the console:

 *for name, obj in bpy.data.objects.items(): obj.data.name = name*



___
### Full Remeshing
Instead of cleaning your mesh (see below) you can just remesh the entire mesh. This is useful but might also cause loss of thin structures, geometry etc. Therefore, if you choose this option, carefully check your model to ensure no features have been smoothed over. In general I have found the **voxel remesher** to work well.

**Voxel Remesher**
Press F3 to bring up the search bar, then type in "voxel remesh". The voxel remesher will create a new mesh based on the volume of your old mesh, ensuring even vertex spacing (which is really useful for FEA analyses).

**Voxel Remesher via Remesh Modifier**
For a bit more control over the voxel modifier, you can apply it via the **remesh modifier**. This can be found under the modifier tab under the wrench symbol when the object is highlighted in the object hierarchy. [**insert remesh modifier image here**]

Note that you need to "apply" any modifiers before exporting this mesh. Applying the modifier means the initial mesh is destroyed and the modifier cannot be adjusted anymore, so make sure the mesh is how you want it before pressing "apply" (under the little downward pointing arrow next to the camera symbold). Before applying the modifier, you can only see the changes in object mode (the mesh in edit mode is only changed once you hit apply). 

The voxel remesher gives the option of adjusting the voxel size for the new mesh.

There are also other options in the remesh modifer (block, smooth, and sharp). Octree depth = 12 sometimes works well but in general the voxel remesh produces much better models. 

___
### Smoothing Sculpting Tool  
The smoothing sculpting tool (in Sculpt mode) can be really useful if you want to locally smoothe an area (for example if there is jagged geometry). There is even an option to mirror the effects, so if your model is symmetrical about the X axis for example, you can select this: [**insert symbol mirror X axis**] and then all of your smoothing that you perform on one side of the model will also be performed on the other side.

___
### Fixing Non-Manifold Meshes
You can check for non-manifold elements in Edit mode under Select > Select by Trait > Non-manifold. A little window will pop up so you can check the different types of non-manifold issues. Sometimes it helps to move edges or vertices in the problematic areas around, so see if maybe the issue is duplicate vertices or edges in the same spot. 

- To solve duplicate vertices or edges, you can use the "merge by distance" tool (Mesh > Clean up > Merge by distance and adjust the values so you only merge those vertices.

- If you have any holes in your mesh, you can try the automatic cleanup tool under Mesh > Clean up > Fill holes. You can also 



___
### Checking for Sharp Triangles and Fixing Them
*Thank you to Niccolo Fioritti for helping write the angle selector code*

To select angles < 20 or >150, go into object mode, select your object, and then run [this script]() in the Python console. Then go into edit mode to view the angles. You can then manually move vertices by clicking on them and dragging them around with the move tool. You can also select the problematic vertex and some surrounding vertices and apply the selective vertex smoothing tool (see below).
___
### ___
### Selective Smoothing of Vertices

