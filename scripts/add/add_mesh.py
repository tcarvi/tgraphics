import bpy
from mathutils import Vector

# Internal method execution
def add_mesh_from_data():

    # TODO - To define input
    scale_x = 1
    scale_y = 1

    # TODO - To define input
    verts = [
        Vector((-1 * scale_x, 1 * scale_y, 0)),
        Vector((1 * scale_x, 1 * scale_y, 0)),
        Vector((1 * scale_x, -1 * scale_y, 0)),
        Vector((-1 * scale_x, -1 * scale_y, 0)),
    ]

    # TODO - To define input
    edges = []

    # TODO - To define input
    faces = [[0, 1, 2, 3]]

    mesh_data = bpy.data.meshes.new(name="MyMeshData")
    mesh_data.from_pydata(verts, edges, faces)
    mesh_object = bpy.data.objects.new(name="MyMeshObject", object_data=mesh_data)
    bpy.context.scene.collection.objects.link(mesh_object)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)

# Class
class ADD_mesh_from_data():
    """Create a new Mesh Object from data: vertices, edges and faces"""

    # Class execution
    def execute():
        print("Adding mesh ...")
        add_mesh_from_data()
        print("Mesh added")

        return {'FINISHED'}

# To register
def register():
    bpy.utils.register_class(ADD_mesh_from_data)

# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_mesh_from_data)

# Register
if __name__ == "__main__":
    register()