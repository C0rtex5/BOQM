bl_info = {
    "name": "BOQM",
    "description": "Blender Object Quick Menu",
    "author": "c0rtex",
    "version": (0, 0, 1),
    "blender": (4, 0, 0),
    "location": "Productivity",
    "warning": "This addon is in its alpha development.",
    "category": "Add Mesh"
}

import bpy
from bpy.types import Menu
class VIEW3D_PT_BOQM(bpy.types.Panel):

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bl_category = "BOQM"
    bl_label = "Blender Mesh Quick Tool"

def draw(self, context):
        """define the layout of the panel"""
        layout = self.layout

        layout.row().operator("mesh.primitive_cube_add", text="Add Cube")
        layout.row().operator("mesh.primitive_uv_sphere_add", text="Add UV Sphere")
        layout.row().operator("mesh.primitive_cylinder_add", text="Add Cylinder")
        layout.row().operator("mesh.primitive_cone_add", text="Add Cone")
        layout.row().operator("mesh.primitive_ico_sphere_add", text="Add Icosphere")
        layout.row().operator("mesh.primitive_plane_add", text="Add Plane")
        layout.row().operator("mesh.primitive_monkey_add", text="Add Monkey")
        layout.row().operator("mesh.primitive_torus_add", text="Add Torus")