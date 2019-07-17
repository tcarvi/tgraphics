bl_info = {
    "name": "New Object from data",
    "author": "Eduardo dos Santos Leal",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > Add object from data",
    "description": "Adds a new Mesh Object from data: vertices, edges and faces",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}

import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

# Internal method execution
def add_object_from_data(self, context):
    scale_x = self.scale.x
    scale_y = self.scale.y

    verts = [
        Vector((-1 * scale_x, 1 * scale_y, 0)),
        Vector((1 * scale_x, 1 * scale_y, 0)),
        Vector((1 * scale_x, -1 * scale_y, 0)),
        Vector((-1 * scale_x, -1 * scale_y, 0)),
    ]

    edges = []
    faces = [[0, 1, 2, 3]]

    mesh = bpy.data.meshes.new(name="New Object Mesh")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)

# Class
class ADD_object_from_data(Operator, AddObjectHelper):
    """Create a new Mesh Object from data: vertices, edges and faces"""
    bl_idname = "mesh.add_object_from_data"
    bl_label = "1- Add mesh object from data"
    bl_options = {'REGISTER', 'UNDO'}

    scale: FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )

    context_override = bpy.context.copy()
    # context_override['selected_objects'] = list(bpy.context.scene.objects)
    # bpy.ops.object.delete(context_override)

    def execute(self, context_override):
        print(context_override)
        print("teste")
        add_object_from_data(self, context_override)

        return {'FINISHED'}

# For buttom Registration: "View3D > Add > Mesh > Add object from data"
def add_object_from_data_button(self, context):
    self.layout.operator(
        ADD_object_from_data.bl_idname,
        text="Add mesh object from data",
        icon='PLUGIN')

# For docs Registration: right click on the button
def add_object_from_data_manual_map():
    url_manual_prefix = "https://docs.blender.org/manual/en/latest/"
    url_manual_mapping = (
        ("bpy.ops.mesh.add_object_from_data", "scene_layout/object/types.html"),
    )
    return url_manual_prefix, url_manual_mapping

# To register
def register():
    bpy.utils.register_class(ADD_object_from_data)
    bpy.utils.register_manual_map(add_object_from_data_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_from_data_button)

# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_object_from_data)
    bpy.utils.unregister_manual_map(add_object_from_data_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_from_data_button)

if __name__ == "__main__":
    register()