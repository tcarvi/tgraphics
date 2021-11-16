import sys
import bpy
import json
import math
import bmesh
from mathutils import Vector, Matrix

t_data_MeshesInitial = bpy.data.meshes.new(name="t_data_MeshesInitial")
# bpy.data.meshes['t_data_MeshesInitial']
t_data_MeshesInitial.from_pydata([Vector((0,0,0)),Vector((1,0,0))],[(0,1)],[])
# bpy.data.meshes['t_data_MeshesInitial']

t_bmesh = bmesh.new(use_operators=True)
t_bmesh.from_mesh(t_data_MeshesInitial)

#
# Operações no BMESH
#

bmesh.ops.extrude_edge_only(t_bmesh)
# t_bmesh.from_object(object=t_object, depsgraph=bpy.context.evaluated_depsgraph_get())
# modifier = t_object.modifiers.new(name="Skin", type='SKIN')

# Finish up, write the bmesh into a new mesh and free the bmesh
t_data_Meshes = bpy.data.meshes.new("t_data_Meshes")
t_bmesh.to_mesh(t_data_Meshes)
t_bmesh.free()

t_object = bpy.data.objects.new(name="t_data_objects",object_data=t_data_Meshes)
# bpy.data.objects['t_data_objects']
print(t_object)
print("verts0 = ", t_data.vertices[0].co)
print("verts1 = ", t_data.vertices[1].co)
AddMaterial.add(t_object, "MaterialretanguloBranca")
bpy.context.scene.collection.objects.link(t_object)