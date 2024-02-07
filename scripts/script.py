# importing

import bpy

bpy.ops.mesh.primitive_cube_add

cube_obj = bpy.context.active_object
cube_obj.location.z = 0