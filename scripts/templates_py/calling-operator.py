

# import bpy

# bpy.ops

# Provides python access to calling operators, this includes operators written in C, Python or macros.
# Only keyword arguments can be used to pass operator properties.
# Operators don’t have return values as you might expect, instead they return a set() which is made up of: {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'}. Common return values are {'FINISHED'} and {'CANCELLED'}.
# Calling an operator in the wrong context will raise a RuntimeError, there is a poll() method to avoid this problem.

# Note that the operator ID (bl_idname) in this example is mesh.subdivide, bpy.ops is just the access path for python.
# Keywords and Positional Arguments
# For calling operators keywords are used for operator properties and positional arguments are used to define how the operator is called.

# There are 3 optional positional arguments.
# bpy.ops.test.operator(override_context, execution_context, undo)
# override_context - dict type.
# execution_context - str (enum).
# undo - bool type.
# Each of these arguments is optional, but must be given in the order above.

# calling an operator
# bpy.ops
# bpy.ops.mesh.subdivide(number_cuts=3, smoothness=0.5)

# check poll() to avoid exception
# bpy.ops
# if bpy.ops.object.mode_set.poll():
#     bpy.ops.object.mode_set(mode='EDIT')

# Overriding Context
# It is possible to override context members that the operator sees, so that they act on specified rather than the selected or active data, 
# or to execute an operator in the different part of the user interface.
# The context overrides are passed as a dictionary, with keys matching the context member names in bpy.context. 
# For example to override bpy.context.active_object, you would pass {'active_object': object}.

# You will nearly always want to use a copy of the actual current context as basis (otherwise, you’ll have to find and gather all needed data yourself).
# remove all objects in scene rather than the selected ones
# import bpy
# context_override = bpy.context.copy()
# context_override['selected_objects'] = list(bpy.context.scene.objects)
# bpy.ops.object.delete(context_override)

# import bpy
# from bpy.types import Operator
# from bpy.props import FloatVectorProperty
# from bpy_extras.object_utils import AddObjectHelper, object_data_add
# from mathutils import Vector
# bpy_extras.object_utils.object_data_add(context, obdata, operator=None, name=None)