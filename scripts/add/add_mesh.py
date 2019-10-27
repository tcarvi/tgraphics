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
    bpy.context.scene.cursor.location[0] += xLocPlus
    bpy.context.scene.cursor.location[1] += yLocPlus
    bpy.context.scene.cursor.location[2] += zLocPlus
    bpy.context.view_layer.update()


def incrementCursorRotationEuler(xRotEulerPlus, yRotEulerPlus, zRotEulerPlus):
    bpy.context.scene.cursor.rotation_euler[0] += xRotEulerPlus
    bpy.context.scene.cursor.rotation_euler[1] += yRotEulerPlus
    bpy.context.scene.cursor.rotation_euler[2] += zRotEulerPlus
    bpy.context.view_layer.update()


# Internal method execution
def add_object(s):

    print("structure [0][0-2] = deslocamentoD0 =")
    print(s[0][0][0])
    print(s[0][0][1])
    print(s[0][0][2])
    print("structure [0][1][0-3][0-2] = verticesD0 =")
    print(s[0][1][0][0])
    print(s[0][1][0][1])
    print(s[0][1][0][2])
    print(s[0][1][1][0])
    print(s[0][1][1][1])
    print(s[0][1][1][2])
    print(s[0][1][2][0])
    print(s[0][1][2][1])
    print(s[0][1][2][2])
    print(s[0][1][3][0])
    print(s[0][1][3][1])
    print(s[0][1][3][2])
    print("structure [0][2] = edgesD0 =")
    print(s[0][2])
    print("structure [0][3][0-3] = facesD0 =")
    print(s[0][3][0])
    print(s[0][3][1])
    print(s[0][3][2])
    print(s[0][3][3])

    # store the location of current 3d cursor
    saved_location = bpy.context.scene.cursor.location.copy()
    saved_rotation = bpy.context.scene.cursor.rotation_euler.copy()

    # TODO - To define input values from same origin
    # Mesh data:
    # Vertex1 = Vector((x, y, z))
    # Vertex2 = Vector((x, y, z))
    # Vertex3 = Vector((x, y, z))
    # Vertex4 = Vector((x, y, z))
    # verts = [
    #     Vertex1,
    #     Vertex2,
    #     Vertex3,
    #     Vertex4,
    # ]
    # edges = []
    # faces = [[0, 1, 2, 3]]

    originX = 0.00
    originY = 0.00
    originZ = 0.00
    setInitialCursorPosition(
        'XYZ',
        [originX, originY, originZ],
        [0.00, 0.00, 0.00]
    )

    # D0
    incrementCursorLocation(s[0][0][0], s[0][0][1], s[0][0][2])
    verticesParede1Coluna1 = [
        Vector((s[0][1][0][0],s[0][1][0][1],s[0][1][0][2])),
        Vector((s[0][1][1][0],s[0][1][1][1],s[0][1][1][2])),
        Vector((s[0][1][2][0],s[0][1][2][1],s[0][1][2][2])),
        Vector((s[0][1][3][0],s[0][1][3][1],s[0][1][3][2]))
    ]
    edgesParede1Coluna1 = [s[0][2]]
    facesParede1Coluna1 = [[s[0][3][0],s[0][3][1],s[0][3][2],s[0][3][3]]]
    mesh_data_P1C1 = bpy.data.meshes.new(name="meshData_P1C1")
    mesh_data_P1C1.from_pydata(
        verticesParede1Coluna1,
        edgesParede1Coluna1,
        facesParede1Coluna1
    )
    mesh_object_P1C1 = bpy.data.objects.new(
        name="meshObject_P1C1",
        object_data=mesh_data_P1C1
    )
    # set the origin on the current object to the 3dcursor location
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.context.scene.collection.objects.link(mesh_object_P1C1)


    # D1
    incrementCursorLocation(s[1][0][0], s[1][0][1], s[1][0][2])
    verticesParede1 = [
        Vector((s[1][1][0][0],s[1][1][0][1],s[1][1][0][2])),
        Vector((s[1][1][1][0],s[1][1][1][1],s[1][1][1][2])),
        Vector((s[1][1][2][0],s[1][1][2][1],s[1][1][2][2])),
        Vector((s[1][1][3][0],s[1][1][3][1],s[1][1][3][2]))
    ]
    edgesParede1 = [s[1][2]]
    facesParede1 = [[s[1][3][0],s[1][3][1],s[1][3][2],s[1][3][3]]]
    mesh_data_P1 = bpy.data.meshes.new(name="meshData_P1")
    mesh_data_P1.from_pydata(
        verticesParede1,
        edgesParede1,
        facesParede1
    )
    mesh_object_P1 = bpy.data.objects.new(
        name="meshObject_P1",
        object_data=mesh_data_P1
    )
    # set the origin on the current object to the 3dcursor location
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.context.scene.collection.objects.link(mesh_object_P1)

    # D3
    incrementCursorLocation(0.0, 8.20, 0.00)
    verticesParede1Coluna2 = [
        Vector((0.00, 0.00, 0.00)),
        Vector((0.00, 0.15, 0.00)),
        Vector((0.15, 0.15, 0.00)),
        Vector((0.15, 0.00, 0.00))
    ]
    edgesParede1Coluna2 = []
    facesParede1Coluna2 = [[0, 1, 2, 3]]
    mesh_data_P1C2 = bpy.data.meshes.new(name="meshData_P1C2")
    mesh_data_P1C2.from_pydata(
        verticesParede1Coluna2,
        edgesParede1Coluna2,
        facesParede1Coluna2
    )
    mesh_object_P1C2 = bpy.data.objects.new(
        name="meshObject_P1C2",
        object_data=mesh_data_P1C2
    )
    # # set the origin on the current object to the 3dcursor location
    # bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.context.scene.collection.objects.link(mesh_object_P1C2)

    # set 3dcursor location back to the stored location
    bpy.context.scene.cursor.location = saved_location
    bpy.context.scene.cursor.rotation_euler = saved_rotation

    # oX =  0.00
    # oY = oY + 13.00
    # oZ = oZ +  0.00
    # parede2 = [
    #     Vector((0.00, 0.00, 0.00)),
    #     Vector((0.00, 7.00, 0.00)),
    #     Vector((0.15, 7.00, 0.00)),
    #     Vector((0.15, 0.00, 0.00))
    # ]
    # oX =  0.15
    # oY = oY +  6.85
    # oZ = oZ +  0.00
    # parede3 = [
    #     Vector((0.00, 0.00, 0.00)),
    #     Vector((0.00, 0.15, 0.00)),
    #     Vector((0.15, 7.00, 0.00)),
    #     Vector((0.15, 0.00, 0.00))
    # ]
    # verts = [
    #     Vector((0, 0, 0)),
    #     Vector((0, 20, 0)),
    #     Vector((25, 20, 0)),
    #     Vector((23, 0, 0)),
    #     Vector((15, -2, 0))
    # ]

    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)


# Class
class ADD_mesh():
    """Create a new Mesh Object from data: vertices, edges and faces"""

    # Class execution
    def execute(structure):
        add_object(structure)
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
