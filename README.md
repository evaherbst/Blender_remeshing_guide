# Blender Mesh Cleaning Guide 
[![FEZ](https://img.shields.io/badge/FEZ-contributor-brightgreen)](https://github.com/FEZ-Finite-Element-Zurich)

For FEA (finite element analysis) and also other goals such as animating or 3D printing, it is important to have clean meshes.
This guide offers step by step instructions to clean your meshes in the freeware Blender, which can be downloaded [here](https://www.blender.org/).

*This guide was created for Blender 2.9. Other versions might have slightly different settings*

**Aims of Mesh Cleaning**:
By cleaning a mesh, we want to make it watertight (e.g. no holes) and **manifold**. Manifold meshes mean that there are no problems such as faces with 0 area, edges connecting more than 2 faces, several vertices occupying the same position, etc. For finite element analysis, we also want to have the elements of the mesh be fairly uniform in size, and to avoid sharp triangles (angles of < 20 degrees and > 150 degrees). This practical guide will teach you how to create a mesh meeting all of these conditions.

A [Youtube tutorial](https://youtu.be/XzAUn76NLXM) is also available (note that the more recent methods using sculpt tools are not included here)

Please also see our paper [paper](https://doi.org/10.1098/rsos.220519) on bone retrodeformation. Sculpting tools can also be used to remesh areas (eg changing resolution) - turn on dynamic topology to do this.
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
- In edit mode, it can be really useful to hide specific faces so you can look at internal geometry etc. To do so, select them with the lasso tool and then press H. Use ALT + H to unhide all.
- Hold down SHIFT to select multiple elements
- F3 will pull up the search menu, so you can type in the same of any tool to search for it
- When you press the Delete key, you get several options. If you want to delete all of that selected geometry, select "Delete Vertices" because if only delete edges or faces the vertices will remain. Deleting only Faces or edges can be useful when you are adjusting the mesh.


### Some useful shortcuts/tools/settings:
- Tool option dialogue: Notice that sometimes the dialogue box for a tool won’t show up, or only after you apply the tool? You can fix this by pressing F9 to immediately see the mathematical options (for example if you want to rotate by 90 degrees about the X axis, you can type these values in the dialogue box).
- You can make your own shortcuts by right clicking on the operation in the menu, and clicking “assign shortcut”
- Tip: if you rename your object, your mesh will often still have the old mesh. (The  object is indicated by the orange upside down triangle in the hierarchy, and the mesh (indicated by the green upside down triangle). To set the name of all meshes to be the same as the object, go to scripting mode and paste the following Python script in the console:

 *for name, obj in bpy.data.objects.items(): obj.data.name = name*

### Before starting:
*Make sure you enable the statistics module. Click on this symbol: ![alt text](https://github.com/evaherbst/Blender_remeshing_guide/blob/main/images%20for%20workflow/statistics_option.JPG)
and then check Statistics.
This will let you know how many elements are selected (which is very useful for your mesh checks).

*For all of these steps, you need to make sure your object is selected.
___
### Full Remeshing 
Instead of cleaning your mesh (see below) you can just remesh the entire mesh. This is useful but might also cause loss of thin structures, geometry etc. Therefore, if you choose this option, carefully check your model to ensure no features have been smoothed over. If your mesh has big holes the remesher doesn't work well, so fix those first. Small holes can be ok (for example if you are trying to merge two objects and there is a small gap between them), but in those cases be sure to check that area of the mesh afterwards because it may need some adjustments such as smoothing.
The voxel remesher is especially useful for combining multiple meshes into one manifold object.

**UPDATE:** I did some test comparing the results of remeshing with desired voxel size versus remeshing at higher resolution and then decimating. Remeshing to desired voxel size sometimes obscures features. Remeshing at higher resolution (e.g. smaller voxel size than you want in the end) followed by decimating is a better way to preserve these features. However, the decimated meshes usually have a less even face distribution (e.g. larger face size differences and sharp triangles). For an even face distribution, see tips on the remeshing tools within the Sculpt Tool below. 

**UPDATE 2:** The remeshing options within the Sculpt Tool (see below) work even better especially if you want to create a triangular mesh.

**Voxel Remesher** (creates quad mesh)
In object mode, press F3 to bring up the search bar, then type in "voxel remesh". The voxel remesher will create a new mesh based on the volume of your old mesh, ensuring even vertex spacing (which is really useful for FEA analyses). 
*If you want more control over the voxel remesher, select your object, go to sculpt mode, then click the tool symbol on the right hand side of the screen. Scroll down to "remesh" (and make sure dyntopo is not checked). Here you can choose voxel size etc, and can even use the eye dropper tool to choose another object as a reference for voxel size. Note that the resulting mesh will be a quad mesh, so if you use a triangulated mesh as a reference, you won't necessarily end up with the same sized triangles. In that case it's sometimes easiest to just adjust the voxel size values instead of using a reference mesh.*

**Voxel Remesher via Remesh Modifier** (creates quad mesh)
For a bit more control over the voxel modifier, you can apply it via the **remesh modifier** in object mode. This can be found under the modifier tab under the wrench symbol when the object is highlighted in the object hierarchy. 

![alt text](https://github.com/evaherbst/Blender_remeshing_guide/blob/main/images%20for%20workflow/remesh_modifier.png)  

Note that you need to "apply" any modifiers before exporting this mesh. Applying the modifier means the initial mesh is destroyed and the modifier cannot be adjusted anymore, so make sure the mesh is how you want it before pressing "apply" (under the little downward pointing arrow next to the camera symbold). Before applying the modifier, you can only see the changes in object mode (the mesh in edit mode is only changed once you hit apply). 

The voxel remesher gives the option of adjusting the voxel size for the new mesh.

There are also other options in the remesh modifer (block, smooth, and sharp). Octree depth = 12 sometimes works well but in general the voxel remesh produces much better models. 

**Decimating** 
Sometimes the resolution of the mesh will be too high for the remesher to work. In this case, you can use a decimate modifier and adjust the slider to get the resolution you want. Then apply the modifier as described above. In some cases decimating and remeshing in Meshlab might be better (try it if Blender crashes a lot due to a very high res mesh).

___
### Remeshing via Sculpting Tools
*Thanks to ![Matt Humpage](https://www.northernroguestudios.com/) for these tips!*

Remeshing via sculpting tools can help clean up meshes both locally (by enabling Dynamic Topology and setting the sculpt tool strength to 0, then going over that area) as well as globally (remeshing via Flood Fill, which can be accessed under Dynamic Topology>Constant Detail). The latter gives a mesh with evenly sized triangular faces.

___
### Smoothing Sculpting Tool  
The smoothing sculpting tool (in Sculpt mode) can be really useful if you want to locally smoothe an area (for example if there is jagged geometry). There is even an option to mirror the effects, so if your model is symmetrical about the X axis for example, you can select this: ![alt text](https://github.com/evaherbst/Blender_remeshing_guide/blob/main/images%20for%20workflow/mirror_X_axis.PNG) and then all of your smoothing that you perform on one side of the model will also be performed on the other side.

___
### Fixing Non-Manifold Meshes
*Also see Sculpt Tool Dynamic Topology methods above, which can help clean the mesh*

You can **check for non-manifold elements** in Edit mode under Select > Select by Trait > Non-manifold. This can be done for both *vertices* and *edges*. A little window will pop up so you can check the different types of non-manifold issues. Sometimes it helps to move edges or vertices in the problematic areas around, so see if maybe the issue is duplicate vertices or edges in the same spot. This is where the Statistics view option comes in handy - you can see how many elements are non-manifold. When you are done cleaning your mesh should have 0 non-manifold elements.

- To solve **duplicate vertices**, you can use the "merge by distance" tool (Mesh > Clean up > **Merge by Distance** and adjust the values so you only merge those vertices.

- You can also remove **duplicate vertices or edges or faces** that are floating with the Mesh > Clean up > **Delete Loose** option. 

- To **remove zero area faces and zero length edges**, use Mesh > Clean up > **Degenerate Dissolve**. 

- If you have any **holes** in your mesh, you can try the automatic cleanup tool under Mesh > Clean up > Fill holes. You can also manually select the surrounding vertices and then fill the gap by pressing F. If you have a big hole bordered by many edges, see section **Manually creating New Faces** below. You can also create a new edge between two selected vertices in the same way. 
 - Depending on the geometry of your gap, you might also want to fill it using "vertex snapping". Select one vertex and drag it over to the vertex you want to connect it to. Select this option ![alt text](https://github.com/evaherbst/Blender_remeshing_guide/blob/main/images%20for%20workflow/vertex_snapping.JPG) and then in the dropdown menu select what you want it to snap to, in this case vertices. Make sure to merge the vertices after snapping them using the Merge by Distance Tool. 

- If you have **floating bits** outside of your model (maybe from your segmentation) then you can remove these by clicking on a vertex or face in the main model (the part you want to keep), then Select > Select Linked (or use CNTL L), and then Select > Invert (or use CNTRL I). This will select only the floating elements that are not connected to your main model. You can delete them (Delete > **Vertices**).

- If you have issues with **non-contiguous** areas (check which types of non-manifold issues are present in the select non-manifold window), this means the adjacent faces have oppostite normals. To fix this, select the surrounding faces (or the entire mesh) and go to Mesh > Normals > Recalculate Outside. 

**3D Print Add-On** This [add-on](https://docs.blender.org/manual/en/latest/addons/mesh/3d_print_toolbox.html?highlight=print) can also be used for mesh inspection and corrections. (thanks Peter Falkingham for pointing this out!). It has an automatic "make manifold" option and can run a lot of checks - however, I prefer to see the problematic areas myself and fix them as in the steps below, to ensure no structures are getting smoothed over. It is super quick and useful though. It also helps to check for 0 area faces and 0 length edges and intersecting faces- see below.

___
### Checking for Self-Intersections

Use the 3D Printing Blender Add-on, click "intersections", fix these.

___
### Selective Smoothing of Vertices

The vertex smoothing tool makes the vertices and angles more evenly spaced. Select the vertices of interest and then Vertex > Smooth Vertices. You can adjust the level of smoothing. You can also select the entire model (press A) and then smooth all vertices. If you do the latter, you should check to make sure no fine structures are lost.

___
### Creating new faces and edges to fill large holes

There may be cases where you deleted some vertices (for example if there was a spiky geometry) and have a big hole that you need to fill, rather than a single triangle. Instead of selecting all of the edges in the perimeter one by one to fill the gap, you can select a single edge and then go to Select > Select Loops > Edge Loops. This will select the perimeter. Then press F to fill the gap. You now will have a big, non triangular gap:  
![alt text](https://github.com/evaherbst/Blender_remeshing_guide/blob/main/images%20for%20workflow/filled_hole.JPG)

You now have two options - 1) you can Triangulate Faces (Face > Triangulate or CNTRL T) or 2) you can manually position edges. 

With option 1), you will likely get sharp triangles:  
![alt text](https://github.com/evaherbst/Blender_remeshing_guide/blob/main/images%20for%20workflow/fill_hole_triangulate.JPG)

You can fix these sometwhat with the "smooth vertices" tool (see above), but the number of triangles is set, so we still don't get super even triangles:  
![alt text](https://github.com/evaherbst/Blender_remeshing_guide/blob/main/images%20for%20workflow/fill_hole_smoothed.JPG)

It is up to you to decide if these are good enough for your model - often they will be, but sometimes you might want to manually create the faces. To do this, fill the hole as above, then use the knife tool to draw edges (enabling the vertex snap option helps with this). Here you can see how I started to draw in the new edges with the knife tool:  

![alt text](https://github.com/evaherbst/Blender_remeshing_guide/blob/main/images%20for%20workflow/filled_hole_manually_knifetool.JPG)

To create new faces, also check out Blender's F2 plug-in (which comes with Blender).


*Sometimes the knife tool might not work well - I think this is when the faces are not planar, so first go to Mesh > Clean up > Make Planar Faces. 
___
### Checking for 0 area faces and 0 length edges
While Blender enables you to fix these, if you want to view them first, the only way I've found is through the 3D print add-on (see above).
Faces with 0 area and edges with 0 length are usually referred to as "degenerate". You can check for them with the 3D print add-on under check > degenerate (and put 0 for the threshold). The add-on will tell you the number of problematic faces and edges - click on that to select them. To clean them, go to Mesh > Clean up > Degenerate Dissolve. You can also use the add-on to check for really small faces that you might want to remove - to do this, adjust the threshold to the desired amount.

___
### Intersecting faces
Use the 3D print add-on to identify intersecting faces, then fix manually.
___
### T-junctions 
If you triangulate your faces, this should correct any T-junctions.

___
### Checking for self intersections
The mesh analysis tool is really useful to highlight regions where there are self-intersections.
https://docs.blender.org/manual/en/latest/modeling/meshes/mesh_analysis.html
___
### Checking for Sharp Triangles and Fixing Them
*Thank you to Niccolo Fioritti for helping write the angle selector code*

First, make sure your mesh is a tri mesh instead of a quad mesh. To triangulate faces, in Edit mode press A with the select tool active to select all faces, then go to Face > Triangulate Faces

**UPDATE**: ![Matt Humpage](https://www.northernroguestudios.com/) kindly implemented my checking sharp angles script as a Blender Plugin, which is much more convenient than running the script manually as described below. The plugin can be installed by simply downloading the file "CheckSharpAngles1.py". Then follow the same steps below (but skip the running the script part, instead press the button in the add-on in object mode). The Add-on automatically creates the vertex group described below.

To select angles < 20 or >150, go into object mode, select your object, and then run [this script](https://github.com/evaherbst/Blender_remeshing_guide/blob/main/Select_Angles_Python_Script.txt) by copying and pasting it into the Python console (in Scripting mode). Then go into edit mode to view the angles. You can then manually move vertices by clicking on them and dragging them around with the move tool. You can also select the problematic vertex and some surrounding vertices and apply the selective vertex smoothing tool (see below). You can also automatically expand the selection of sharp triangles by 1 vertex in each direction and then smooth. You can also use the vertex smoothing tool on the whole model but ensure that no details are lost (see below). Merge by distance can also be useful, although be careful that you do not merge vertices that you didn't intend to merge.

I usually go through the angles one by one to fix them (either with selective vertex smoothing or manually). 
If you decide to fix the angles one by one (instead of using the vertex smoothing on the whole model), then it helps to save the results of the script using **vertex groups**. Vertex groups essentially allow you to save a group of selected vertices (so in this case, once you've fixed on angle, you don't need to rerun the script to select the remaining angles, but can just select the vertex group. The angles you fixed will still be part of the vertex group but it should be easy to see which ones are still problematic (i.e. very sharp triangles). I usually use the vertex group, fix several angles, and after a while re-run the script, and save the selection again as a vertex group to work through the remaining issues.

To create a vertex group, in Edit mode (with the vertices selected by the angle script), go to the vertex properties tab and press the plus icon:
![alt text](https://github.com/evaherbst/Blender_remeshing_guide/blob/main/images%20for%20workflow/vertex_groups_v2.JPG)

Type in the name for the group (for example "sharp angles"). Then press "assign" to assign the problematic vertices to the vertex group.
If you want to update the vertex group (after cleaning some sharp angles), in the vertex group go to select, then remove. Now your vertex group is empty and you can rerun the script and assign the remaining sharp angle vertices to that group. 

Keep fixing vertices until the script results in 0 selected vertices (this means no angles are > 150 or < 20 degrees). As mentioned above, make sure the Statistics view is enabled so you can see the number of vertices selected by the script.

**note**: if you get an error that says edges of size 0 are causing a problem, use the "merge by distance" feature to clean these up, then rerun the script again.

___
### Merging two objects
To merge objects (for example if you reassembled two bone fragments) you can join them or use a Boolean union modifier (under modifiers), and then remesh. The Boolean union essentially joins the two objects but removes internal geometry - however, if your meshes don't have good overlap you usually still have to clean up the seam area where the two meshes are joined *and often the internal geometry is not removed properly, so be careful and check!*

___
### After all your mesh adjustments, run the non-manifold checks again to make sure no errors were introduced during your mesh cleaning.

___
### Note about exports!

You will probably be exporting your model as an .stl or .obj. Note that during export you need to check which axes are set to "up" and "forward"! Make sure the axes match your scene (or, alternatively, if you want to change which axis is up and which is forward your FEA model (or whatever other program you're exporting to), you can set this in the export steps).
