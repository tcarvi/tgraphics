import bpy
from mathutils import Vector
from move_entry_point import MoveEntryPoint


def processar_estrutura(structure):
    # store the location of current 3d cursor
    initial_location = bpy.context.scene.cursor.location.copy()
    initial_rotation = bpy.context.scene.cursor.rotation_euler.copy()

    MoveEntryPoint.centralizar()

    for desenho in structure:
        add_object(desenho)

    # set 3dcursor location back to the stored location
    bpy.context.scene.cursor.location = initial_location
    bpy.context.scene.cursor.rotation_euler = initial_rotation


# Internal method execution
def add_object(d):

    MoveEntryPoint.mover(
        d[0][0],
        d[0][1],
        d[0][2]
    )
    data = bpy.data.meshes.new(name="meshData")
    data.from_pydata(
        [
            Vector((d[1][0][0], d[1][0][1], d[1][0][2])),
            Vector((d[1][1][0], d[1][1][1], d[1][1][2])),
            Vector((d[1][2][0], d[1][2][1], d[1][2][2])),
            Vector((d[1][3][0], d[1][3][1], d[1][3][2]))
        ],
        [
            d[2]
        ],
        [
            [
                d[3][0],
                d[3][1],
                d[3][2],
                d[3][3]
            ]
        ]
    )
    object = bpy.data.objects.new(
        name="meshObject",
        object_data=data
    )
    # set the origin on the current object to the 3dcursor location
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.context.scene.collection.objects.link(object)

    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)


# Class
class AddMesh():
    """Create a new Mesh Object from data: vertices, edges and faces"""

    # Class execution
    def add(structure):
        processar_estrutura(structure)
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(AddMesh)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddMesh)


# Register
if __name__ == "__main__":
    register()
