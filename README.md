# Blender_remeshing_guide
For FEA (finite elemenet analysis) and also other goals such as animating or 3D printing, it is important to have clean meshes.
This guide offers step by step instructions to clean your meshes in the freeware Blender.

Blender can be downloaded [here]
*This guide was created for Blender 2.9. Other versions may have differences in hotkeys*

___
*Before we get into the mesh cleaning, here are some useful Blender shortcuts and tips:*

**Useful Blender hotkeys:**

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


Some useful shortcuts/tools/settings:
- Tool option dialogue: Notice that sometimes the dialogue box for a tool won’t show up, or only after you apply the tool? You can fix this by pressing F9 to immediately see the mathematical options (for example if you want to rotate by 90 degrees about the X axis, you can type these values in the dialogue box).
- You can make your own shortcuts by right clicking on the operation in the menu, and clicking “assign shortcut”
- Tip: if you rename your object, your mesh will often still have the old mesh. (The  object is indicated by the orange upside down triangle in the hierarchy, and the mesh (indicated by the green upside down triangle). To set the name of all meshes to be the same as the object, go to scripting mode and paste the  following Python script in the console:

 *for name, obj in bpy.data.objects.items(): obj.data.name = name*

The smoothing sculpting tool (in Sculpt mode) can be really useful if you want to locally smoothe an area (for example if there is jagged geometry). There is even an option to mirror the effects, so if your model is symmetrical about the X axis for example, you can select this:     and then all of your smoothing that you perform on one side of the model will also be performed on the other side.






Manually cleaning meshes by moving vertices, filling in geometry, etc:

Smooth vertices: ctrl + V to bring up the vertex menu, select Smooth Vertices, then hold down shift + R, adjust slider 

Merge vertices : select vertices, ALT + M > select “At last”

Add a face between edges or vertices, or add a new edge between two vertices (e.g. if there is a hole): select edges (or vertices), click F




Delete floating faces/loose pieces:
edit mode>select>select linked > click on main body
then select>invert and delete vertices, edges, faces


Get rid of duplicate vertices:
By selecting all vertices, right clicking, merge>by distance. The default distance is 0 so it will remove duplicate vertices. 

Bridge Tool: 
This automatically creates geometry to fill in a gap between surfaces. Note that the surfaces need to be one object, so first join the meshes into a single object with CNTRL J. Then select the border loops (for example by selecting edge loops) and press CNTRL E > Bridge Edge Loops.

Snapping:
Useful if you have a gap and want to snap one vertex to another, for example. 
Use this tool, and then in the dropdown menu select what you want it to snap to.
Make sure to merge the vertices after snapping them, using  “ALT + M” or use automerge under “options”). 


Mesh cleaning checks
Can use 3D printer add on (enable in Prefs> add ons> 3D print to see some mesh cleaning options. The check all will run all the checks on the model. Or, you can use select> select by trait> non manifold.


Filling holes in mesh:
See above for adding faces or vertices manually, or using the bridge tool.
Can select non-manifold edges (with edge mode in edit mode)>select by trait> non manifold and then CNTRL F to fill holes
-might not solve all non manifold issues
Angle measurements:
For finite element analysis, we need to remove very thin spiky triangles to make a good mesh for the volumetric model. 


Custom script for selecting triangles with angles < 20 degrees and > 150 in Blender
First, make sure nothing is selected in Edit mode, then go to Object mode

Then go to “scripting” and enter [this Python script] (add link) in the console


Then go back to Edit mode. Triangles with angles < 20 degrees and > 150 will be selected in Edit mode after script runs. 
Angles and corresponding indices are also saved to a file.


