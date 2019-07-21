import bpy


# Internal method execution
def add_object():

    # TODO - To define input
    # TODO - To add
    print("TODO")


# Class
class ADD_image():
    """ADD image with input location"""

    # Class execution
    def execute():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(ADD_image)


# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_image)


# Register
if __name__ == "__main__":
    register()
