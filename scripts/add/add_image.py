import bpy


# Internal method execution
def add_object():

    # TODO - To define input
    # TODO - To add
    print("TODO")


# Class
class AddImage():
    """ADD image with input location"""

    # Class execution
    def add():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(AddImage)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddImage)


# Register
if __name__ == "__main__":
    register()
