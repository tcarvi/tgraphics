import bpy
from mathutils import Vector


# padrão de inicialização
def setInitialCursorPosition(rotation_mode, location, rotation_euler):
    # rotation_mode. Default value = 'XYZ'
    # location. Default value = [0.00, 0.00, 0.00]
    # rotation_euler. Default value = [0.00, 0.00, 0.00]
    bpy.context.scene.cursor.rotation_mode = rotation_mode
    bpy.context.scene.cursor.location[0] = location[0]
    bpy.context.scene.cursor.location[1] = location[1]
    bpy.context.scene.cursor.location[2] = location[2]
    bpy.context.scene.cursor.rotation_euler[0] = rotation_euler[0]
    bpy.context.scene.cursor.rotation_euler[1] = rotation_euler[1]
    bpy.context.scene.cursor.rotation_euler[2] = rotation_euler[2]


def incrementCursorLocation(xLocPlus, yLocPlus, zLocPlus):
    print("bpy.context.scene.cursor.location[0]=")
    print(bpy.context.scene.cursor.location[0])
    print("xLocPlus=")
    print(xLocPlus)
    print("bpy.context.scene.cursor.location[1]=")
    print(bpy.context.scene.cursor.location[1])
    print("yLocPlus=")
    print(yLocPlus)
    print("bpy.context.scene.cursor.location[2]=")
    print(bpy.context.scene.cursor.location[2])
    print("zLocPlus=")
    print(zLocPlus)
    bpy.context.scene.cursor.location[0] += xLocPlus
    bpy.context.scene.cursor.location[1] += yLocPlus
    bpy.context.scene.cursor.location[2] += zLocPlus
    bpy.context.view_layer.update()


def incrementCursorRotationEuler(xRotEulerPlus, yRotEulerPlus, zRotEulerPlus):
    bpy.context.scene.cursor.rotation_euler[0] += xRotEulerPlus
    bpy.context.scene.cursor.rotation_euler[1] += yRotEulerPlus
    bpy.context.scene.cursor.rotation_euler[2] += zRotEulerPlus
    bpy.context.view_layer.update()

def processar_estrutura(structure):
    # store the location of current 3d cursor
    saved_location = bpy.context.scene.cursor.location.copy()
    saved_rotation = bpy.context.scene.cursor.rotation_euler.copy()

    originX = 0.00
    originY = 0.00
    originZ = 0.00
    # originRotEulerX = 0.00
    # originRotEulerY = 0.00
    # originRotEulerZ = 0.00
    setInitialCursorPosition(
        'XYZ',
        [originX, originY, originZ],
        [0.00, 0.00, 0.00]
    )

    for desenho in structure:
        add_object(desenho)
    
    # set 3dcursor location back to the stored location
    bpy.context.scene.cursor.location = saved_location
    bpy.context.scene.cursor.rotation_euler = saved_rotation

# Internal method execution
def add_object(d):
    
    incrementCursorLocation(d[0][0], d[0][1], d[0][2])
    data = bpy.data.meshes.new(name="meshData")
    data.from_pydata(
        [ Vector((d[1][0][0],d[1][0][1],d[1][0][2])),
        Vector((d[1][1][0],d[1][1][1],d[1][1][2])),
        Vector((d[1][2][0],d[1][2][1],d[1][2][2])),
        Vector((d[1][3][0],d[1][3][1],d[1][3][2])) ],
        [d[2]],
        [[d[3][0],d[3][1],d[3][2],d[3][3]]]
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
class ADD_mesh():
    """Create a new Mesh Object from data: vertices, edges and faces"""

    # Class execution
    def execute(structure):
        processar_estrutura(structure)
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(ADD_mesh)


# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_mesh)


# Register
if __name__ == "__main__":
    register()
