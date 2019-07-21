# bpy.ops
#### Calling operators
- Provides python access to calling operators, this includes operators written in C, Python or macros.
- Only keyword arguments can be used to pass operator properties.
- Operators don’t have return values as you might expect, instead they return a set() which is made up of: {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'}. Common return values are {'FINISHED'} and {'CANCELLED'}.
- Calling an operator in the wrong context will raise a RuntimeError, there is a poll() method to avoid this problem.

- In the example ```bpy.ops.mesh.subdivide(number_cuts=3, smoothness=0.5)```, the operator ID (bl_idname) is ```mesh.subdivide```. The term ```bpy.ops``` is just the access path for python.  

#### Keywords and Positional Arguments
- For calling operators, keywords are used for operator properties. And positional arguments are used to define how the operator is called.

#### There are 3 optional positional arguments.
- bpy.ops.test.operator(override_context, execution_context, undo)
    - override_context - dict type.
    - execution_context - str (enum).
    - undo - bool type.
    - Each of these arguments is optional, but must be given in the order above.

```
import bpy  
# calling an operator:  
bpy.ops.mesh.subdivide(number_cuts=3, smoothness=0.5)  
# check poll() to avoid exception  
if bpy.ops.object.mode_set.poll():  
    bpy.ops.object.mode_set(mode='EDIT')  
```  

mesh_data Method
from_pydata(vertices, edges, faces)
Make a mesh from a list of vertices/edges/faces
Parameters:

:arg vertices:
   float triplets each representing (X, Y, Z)
   eg: [(0.0, 1.0, 0.5), ...].
   :type vertices: iterable object

:arg edges:
   int pairs, each pair contains two indices to the vertices argument.
   eg: [(1, 2), ...]
   :type edges: iterable object

:arg faces:
   iterator of faces, each faces contains three or more indices to
   the *vertices* argument. eg: [(5, 6, 8, 9), (1, 2, 3), ...]
   :type faces: iterable object

.. warning::
   Invalid mesh data
   *(out of range indices, edges with matching indices,
   2 sided faces... etc)* are **not** prevented.
   If the data used for mesh creation isn't known to be valid,
   run :class:`Mesh.validate` after this function.

Mesh Data documentation:
The mesh data is accessed in object mode and intended for compact storage
Blender stores 4 main arrays to define mesh geometry.
- Mesh.vertices (3 points in space)
- Mesh.edges (reference 2 vertices)
- Mesh.loops (reference a single vertex and edge)
- Mesh.polygons: (reference a range of loops)
Each polygon reference a slice in the loop array, this way,
  polygons do not store vertices or corner data such as UV’s directly,
  only a reference to loops that the polygon uses.
Mesh.loops, Mesh.uv_layers Mesh.vertex_colors are all aligned so
  the same polygon loop indices can be used to find the UV’s and vertex colors
  as with as the vertices.
Mesh fields:
- edges  (readonly)
- vertices (readonly)