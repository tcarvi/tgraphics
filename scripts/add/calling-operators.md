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
