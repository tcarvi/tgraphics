# <pep8-80 compliant>
import bpy


# Class
class AddImage:
    """ADD image with input location"""

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
    bpy.utils.register_class(AddImage)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddImage)


# Register
if __name__ == "__main__":
    register()
