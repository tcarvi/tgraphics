import bpy
from mathutils import Vector
from move_entry_point import MoveEntryPoint


def processar_estrutura(structure):

    MoveEntryPoint.centralizar()

    for d in structure:
        add_object(d)
        bpy.context.scene.cursor.location[0] += d[1][1][0]
        bpy.context.scene.cursor.location[1] += d[1][1][1]
        bpy.context.scene.cursor.location[2] += d[1][1][2]


# Internal method execution
def add_object(d):

    MoveEntryPoint.mover(
        d[0][0],
        d[0][1],
        d[0][2]
    )
    bpy.context.view_layer.update()
    data = bpy.data.meshes.new(name="meshData")
    data.from_pydata(
        [
            Vector(
                (
                    d[1][0][0] + bpy.context.scene.cursor.location[0],
                    d[1][0][1] + bpy.context.scene.cursor.location[1],
                    d[1][0][2] + bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    d[1][1][0] + bpy.context.scene.cursor.location[0],
                    d[1][1][1] + bpy.context.scene.cursor.location[1],
                    d[1][1][2] + bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    d[1][2][0] + bpy.context.scene.cursor.location[0],
                    d[1][2][1] + bpy.context.scene.cursor.location[1],
                    d[1][2][2] + bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    d[1][3][0] + bpy.context.scene.cursor.location[0],
                    d[1][3][1] + bpy.context.scene.cursor.location[1],
                    d[1][3][2] + bpy.context.scene.cursor.location[2]
                )
            )
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
    bpy.context.scene.collection.objects.link(object)


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
