bl_info = {
    "name": "Check Sharp Angles",
    "author": "Eva Herbst, Niccolo Fioritti, Matt Humpage, 2021/22",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "location": "View3D > UI > Sharp Angles°",
    "description": "Checks for triangles with angles <20° and >150° on active object, opens edit mode, and assigns to Vertex Group 'Sharp Angles'",
    "warning": "",
    "doc_url": "",
    "category": "Analysis",
}
import bpy

def main(context):
    import math
    obj = bpy.context.object

    #deselects any previously selected vertices in Edit mode before running script
    bpy.ops.object.mode_set(mode="EDIT") #Activating Edit mode
    bpy.ops.mesh.select_all(action = 'DESELECT') #Deselecting all
    bpy.ops.object.mode_set(mode="OBJECT") #Going back to Object mode

    def angle_between_edges(obj,poly,e1,e2):
        common_vert = set(e1).intersection(set(e2))
        if common_vert==set():
            return None
        v0 = list(common_vert)[0]
        v1 = list(set(e1).difference(common_vert))[0]
        v2 = list(set(e2).difference(common_vert))[0]
        vec1 = obj.data.vertices[v1].co -obj.data.vertices[v0].co 
        vec2 = obj.data.vertices[v2].co -obj.data.vertices[v0].co 
        angle = vec1.angle(vec2)
        angle = math.degrees(angle)
        return angle
    
    def selectPolygon(angle,polyIndex):
        if(angle is not None):
            if(angle<20 or angle >150):
                obj = bpy.context.active_object
                obj.data.polygons[polyIndex].select = True
    
            
    # 
    # 
        


    for p_i,poly in enumerate(obj.data.polygons):
        for i,e1 in enumerate(poly.edge_keys):
            for j,e2 in enumerate(poly.edge_keys):
                if i<j:
                    angle = angle_between_edges(obj,poly,e1,e2)
                    selectPolygon(angle,p_i)
                    if angle==None:
                        continue

    bpy.ops.object.editmode_toggle()
    group = obj.vertex_groups.new( name = 'Sharp Angles' )
    #group.add(bpy.data.objects.verts, 1.0, 'ADD')
    bpy.ops.object.vertex_group_assign()


class SharpAngles(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "myops.check_sharpangles"
    bl_label = "Check Sharp Angles"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}

class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Analyze"
    bl_idname = "Test"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Sharp Angles"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Check angles <20°, >150°", icon='GROUP_VERTEX')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)


        row = layout.row()
        row.operator("myops.check_sharpangles")

def register():
    bpy.utils.register_class(SharpAngles)
    bpy.utils.register_class(HelloWorldPanel)

def unregister():
    bpy.utils.unregister_class(SharpAngles)
    bpy.utils.unregister_class(HelloWorldPanel)

if __name__ == "__main__":
    register()

    # test call
    # bpy.ops.myops.check_sharpangles()
