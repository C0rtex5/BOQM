import bpy

class VIEW3D_PT_BOQM(bpy.types.Panel):

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bl_label = "Blender object quick menu"

    def draw(self, context):
        """define the layout of the panel"""