# Overriding Context
- It is possible to override context members that the operator sees, so that they act on specified rather than the selected or active data, or to execute an operator in the different part of the user interface.
- The context overrides are passed as a dictionary, with keys matching the context member names in bpy.context.  
- For example: to override bpy.context.active_object, you would pass {'active_object': object}.  

- You will nearly always want to use a copy of the actual current context as basis (otherwise, you’ll have to find and gather all needed data yourself).  
#### Example:  
- Remove all objects in scene rather than the selected ones
# import bpy
context_override = bpy.context.copy()
context_override['selected_objects'] = list(bpy.context.scene.objects)
bpy.ops.object.delete(context_override)