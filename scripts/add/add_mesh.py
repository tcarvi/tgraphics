import bpy
from mathutils import Vector

def setInitialCursorPosition(rotation_mode, location, rotation_euler):
    # rotation_mode. Default value = 'XYZ'
    # location. Default value = [0.00, 0.00, 0.00]
    # rotation_euler. Default value = [0.00, 0.00, 0.00]
    bpy.context.scene.cursor.rotation_mode = rotation_mode
    bpy.context.scene.cursor.location[0]= location[0]
    bpy.context.scene.cursor.location[1]= location[1]
    bpy.context.scene.cursor.location[2]= location[2]
    bpy.context.scene.cursor.rotation_euler[0]= rotation_euler[0]
    bpy.context.scene.cursor.rotation_euler[1]= rotation_euler[1]
    bpy.context.scene.cursor.rotation_euler[2]= rotation_euler[2]
    bpy.context.view_layer.update()

def incrementCursorLocation(xLocPlus, yLocPlus, zLocPlus):
    bpy.context.scene.cursor.location[0] += xLocPlus
    bpy.context.scene.cursor.location[1] += yLocPlus
    bpy.context.scene.cursor.location[2] += zLocPlus
    
def incrementCursorRotationEuler(xRotEulerPlus, yRotEulerPlus, zRotEulerPlus):
    bpy.context.scene.cursor.rotation_euler[0] += xRotEulerPlus
    bpy.context.scene.cursor.rotation_euler[1] += yRotEulerPlus
    bpy.context.scene.cursor.rotation_euler[2] += zRotEulerPlus

# Internal method execution
def add_mesh_from_data():

    # TODO - To define input values from same origin
    # Input data: vectors
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
    originX = 0.00
    originY = 0.00
    originZ = 0.00
    setInitialCursorPosition('XYZ', [originX, originY, originZ], [0.00, 0.00, 0.00])
    verticesParede1Coluna1 = [
        Vector((originX + 0.00, originY + 0.00, originZ + 0.00)),
        Vector((originX + 0.00, originY + 0.15, originZ + 0.00)),
        Vector((originX + 0.15, originY + 0.15, originZ + 0.00)),
        Vector((originX + 0.15, originY + 0.00, originZ + 0.00))
    ]
    edgesParede1Coluna1 = []
    facesParede1Coluna1 = [[0, 1, 2, 3]]
    mesh_data_P1C1 = bpy.data.meshes.new(name="meshData_P1C1")
    mesh_data_P1C1.from_pydata(verticesParede1Coluna1, edgesParede1Coluna1, facesParede1Coluna1)
    mesh_object_P1C1 = bpy.data.objects.new(name="meshObject_P1C1", object_data=mesh_data_P1C1)
    bpy.context.scene.collection.objects.link(mesh_object_P1C1)

    originY += 0.15
    incrementCursorLocation(0.0, 0.15, 0.0)
    verticesParede1 = [
        Vector((originX + 0.00, originY + 0.00, originZ + 0.00)),
        Vector((originX + 0.00, originY + 8.20, originZ + 0.00)),
        Vector((originX + 0.15, originY + 8.20, originZ + 0.00)),
        Vector((originX + 0.15, originY + 0.00, originZ + 0.00))
    ]
    edgesParede1 = []
    facesParede1 = [[0, 1, 2, 3]]
    mesh_data_P1 = bpy.data.meshes.new(name="meshData_P1")
    mesh_data_P1.from_pydata(verticesParede1, edgesParede1, facesParede1)
    mesh_object_P1 = bpy.data.objects.new(name="meshObject_P1", object_data=mesh_data_P1)
    bpy.context.scene.collection.objects.link(mesh_object_P1)

    originY += 8.20
    verticesParede1Coluna2 = [
        Vector((originX + 0.00, originY + 0.00, originZ + 0.00)),
        Vector((originX + 0.00, originY + 0.15, originZ + 0.00)),
        Vector((originX + 0.15, originY + 0.15, originZ + 0.00)),
        Vector((originX + 0.15, originY + 0.00, originZ + 0.00))
    ]
    edgesParede1Coluna2 = []
    facesParede1Coluna2 = [[0, 1, 2, 3]]
    mesh_data_P1C2 = bpy.data.meshes.new(name="meshData_P1C2")
    mesh_data_P1C2.from_pydata(verticesParede1Coluna2, edgesParede1Coluna2, facesParede1Coluna2)
    mesh_object_P1C2 = bpy.data.objects.new(name="meshObject_P1C2", object_data=mesh_data_P1C2)
    bpy.context.scene.collection.objects.link(mesh_object_P1C2)

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

# mesh_data Method
# from_pydata(vertices, edges, faces)
# Make a mesh from a list of vertices/edges/faces
# Parameters:
#
# :arg vertices:
#    float triplets each representing (X, Y, Z)
#    eg: [(0.0, 1.0, 0.5), ...].
#    :type vertices: iterable object
#
# :arg edges:
#    int pairs, each pair contains two indices to the vertices argument. 
#    eg: [(1, 2), ...]
#    :type edges: iterable object
#
# :arg faces:
#    iterator of faces, each faces contains three or more indices to
#    the *vertices* argument. eg: [(5, 6, 8, 9), (1, 2, 3), ...]
#    :type faces: iterable object
#
# .. warning::
#    Invalid mesh data
#    *(out of range indices, edges with matching indices,
#    2 sided faces... etc)* are **not** prevented.
#    If the data used for mesh creation isn't known to be valid,
#    run :class:`Mesh.validate` after this function.


# Mesh Data documentation:
# The mesh data is accessed in object mode and intended for compact storage
# Blender stores 4 main arrays to define mesh geometry.
# - Mesh.vertices (3 points in space)
# - Mesh.edges (reference 2 vertices)
# - Mesh.loops (reference a single vertex and edge)
# - Mesh.polygons: (reference a range of loops)
# Each polygon reference a slice in the loop array, this way, 
#   polygons do not store vertices or corner data such as UV’s directly, 
#   only a reference to loops that the polygon uses.
# Mesh.loops, Mesh.uv_layers Mesh.vertex_colors are all aligned so 
#   the same polygon loop indices can be used to find the UV’s and vertex colors 
#   as with as the vertices.
# Mesh fields:
# - edges  (readonly)
# - vertices (readonly)