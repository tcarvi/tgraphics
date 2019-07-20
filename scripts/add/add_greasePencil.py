import bpy

# Internal method execution
def add_object():

    # TODO - To define input

    # TODO - To add
    
# Class
class ADD_greasepencil():
    """ADD greasepencil with input location"""

    # Class execution
    def execute():
        add_object()
        return {'FINISHED'}

# To register
def register():
    bpy.utils.register_class(ADD_greasepencil)

# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_greasepencil)

# Register
if __name__ == "__main__":
    register()