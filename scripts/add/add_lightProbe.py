import bpy


# Internal method execution
def add_object():

    # TODO - To define input
    locationInput = 2.0, 2.0, 5.0
    # TODO - To add


# Class
class ADD_lightprobe():
    """ADD lightprobe with input location"""

    # Class execution
    def execute():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(ADD_lightprobe)


# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_lightprobe)


# Register
if __name__ == "__main__":
    register()
