import bpy

class VIEW3D_PT_BOQM(bpy.types.Panel):

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bl_category = "BOQM"
    bl_label = "Blender object quick menu"

    def draw(self, context):
        """define the layout of the panel"""
        layout = self.layout

        layout.row().operator("mesh.primitive_cube_add", text="Add Cube")
        layout.row().operator("mesh.primitive_uv_sphere_add", text="Add UV Sphere")
        layout.row().operator("mesh.primitive_cylinder_add", text="Add Cylinder")
        layout.row().operator("mesh.primitive_cone_add", text="Add Cone")
        layout.row().operator("mesh.primitive_ico_sphere_add", text="Add Icosphere")
        layout.row().operator("mesh.primitive_plane_add", text="Add Plane")

def register():
    bpy.utils.register_class(VIEW3D_PT_BOQM)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_BOQM)

if __name__ == "__main__":
    register()