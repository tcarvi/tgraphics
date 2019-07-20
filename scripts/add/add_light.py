import bpy

# Internal method execution
def add_light():

    # TODO - To define input
    locationInput = 2.0, 2.0, 5.0

    # TODO - To add

# Class
class ADD_light():
    """ADD light with input location"""

    # Class execution
    def execute():
        add_light()
        return {'FINISHED'}

# To register
def register():
    bpy.utils.register_class(ADD_light)

# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_light)

# Register
if __name__ == "__main__":
    register()