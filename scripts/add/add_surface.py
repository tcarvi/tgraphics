# <pep8-80 compliant>
import bpy


# Class
class AddSurface():
    """ADD surface with input location"""

    # Class execution
    def add():
        add_object()
        return {'FINISHED'}


# Internal method execution
def add_object():
    # TODO - To define input
    # TODO - To add
    print("TODO")


# To register
def register():
    bpy.utils.register_class(AddSurface)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddSurface)


# Register
if __name__ == "__main__":
    register()
