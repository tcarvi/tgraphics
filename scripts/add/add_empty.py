# <pep8-80 compliant>
import bpy


# Class
class AddEmpty():
    """ADD empty with input location"""

    # Class execution
    @classmethod
    def add(cls):
        add_object()
        return {'FINISHED'}


# Internal method execution
def add_object():
    # TODO - To define input
    # TODO - To add
    print("TODO")


# To register
def register():
    bpy.utils.register_class(AddEmpty)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddEmpty)


# Register
if __name__ == "__main__":
    register()
