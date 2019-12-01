# <pep8-80 compliant>
import bpy


# Internal method execution
def add_object():

    # TODO - To define input
    # TODO - To add
    print("TODO")


# Class
class AddEmpty():
    """ADD empty with input location"""

    # Class execution
    def add():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(AddEmpty)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddEmpty)


# Register
if __name__ == "__main__":
    register()
