import bpy, bmesh
import mathutils

#
# Unlike bpy, a BMesh does not necessarily correspond to data 
# in the currently open blend file,
# a BMesh can be created, edited and freed 
# without the user ever seeing or having access to it.
#


def Drawing():
    bm = bmesh.new()

    for obj in bpy.data.objects:
        if obj.type != 'empty':
            obj.select = False

    return{bm.edges}
    """
    # create vector (0.5,0.5,0.5)
    #centerVector = mathutils.Vector((0.5,0.5,0.5))

    # center vertex (0,0,0)
    #centerVertex = bmesh.ops.create_vert(bm0, co=centerVector)

    # create Matrix Translation for multiplication
    matrixTranslation0 = mathutils.Matrix()
    matrixTranslation0[0][3] = 0.07           # Add to x position
    matrixTranslation0[1][3] = 0.07           # Add to y position
    matrixTranslation0[2][3] = 0.07           # Add to z postion

    #
    # Create cube for Wall, in the intial point
    # Relates the cube to a bmesh
    # Just to the right of the door.
    # 
    cube0 = bmesh.ops.create_cube(bm, size=0.14, matrix=matrixTranslation0)
    print(cube0.get('verts')[0].co)
    print(cube0.get('verts')[1].co)
    print(cube0.get('verts')[2].co)
    print(cube0.get('verts')[3].co)
    print(cube0.get('verts')[4].co)
    print(cube0.get('verts')[5].co)
    print(cube0.get('verts')[6].co)
    print(cube0.get('verts')[7].co)

    #
    # Create a Mesh Data Block in the main database
    # and write a bmesh to this datablock 
    #
    meshDataBlock = bpy.data.meshes.new("Cube")
    bm.to_mesh(meshDataBlock)

    objectToLink0 = bpy.data.objects.new("wall0", meshDataBlock)
    bpy.context.scene.objects.link(objectToLink0)

    #self.deselectObjects()

    bpy.context.scene.objects.active = objectToLink0
    objectToLink0.select = True

    # create Scaling tuple for multiplication
    xValorDesejado = 0.14
    xScale = 0.14/0.14
    yValorDesejado = 0.80
    yScale = 0.80/0.14
    zValorDesejado = 1.0
    zScale = 1.0/0.14

    # resize of cube, by input

    bpy.ops.transform.resize(value=(xScale,yScale,zScale), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)

    bpy.context.scene.update()
    """

Drawing()
"""
def drawingWall2():

    # OPTION
    # create a new BMesh
    # bm1 = bmesh.new()

    # create Matrix Translation for multiplication
    matrixTranslation1 = mathutils.Matrix()
    matrixTranslation1[0][3] = 0.07           # Add to x position
    matrixTranslation1[1][3] = 2.07           # Add to y position
    matrixTranslation1[2][3] = 0.07           # Add to z postion

    cube1 = bmesh.ops.create_cube(bm0, size=0.14, matrix=matrixTranslation1)
    print(cube1.get('verts')[0].co)
    print(cube1.get('verts')[1].co)
    print(cube1.get('verts')[2].co)
    print(cube1.get('verts')[3].co)
    print(cube1.get('verts')[4].co)
    print(cube1.get('verts')[5].co)
    print(cube1.get('verts')[6].co)
    print(cube1.get('verts')[7].co)

    mesh1 = bpy.data.meshes.new("Cube")
    bm0.to_mesh(mesh1)
    objectToLink1 = bpy.data.objects.new("wall1", mesh1)
    bpy.context.scene.objects.link(objectToLink1)

    # create Scaling tuple for multiplication
    xValorDesejado = 0.14
    xScale = 0.14/0.14
    yValorDesejado = 0.80
    yScale = 0.80/0.14
    zValorDesejado = 1.0
    zScale = 1.0/0.14

    # resize of cube, by input

    bpy.ops.transform.resize(value=(xScale,yScale,zScale), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)

    bpy.context.scene.update()


# To Use 
#bm.normal_update()
#bm.transform(matrix, filter=None)  matrix:(4x4 mathutils.Matrix)
#bm.edges   (readonly) Type: BMEdgeSeq
#bm.faces   (readonly) Type: BMFaceSeq 
#bm.verts   (readonly) Type: BMVertSeq
#bm.hide_set(hide)   hide: boolean
"""
