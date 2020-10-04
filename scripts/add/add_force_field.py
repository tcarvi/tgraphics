# <pep8-80 compliant>
import bpy


# Internal method execution
def add_object():
    # TODO - To define input
    # TODO - To add
    print("TODO")


# Class
class AddForceField():
    """ADD forcefield"""

    # Class execution
    def add():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(AddForceField)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddForceField)


# Register
if __name__ == "__main__":
    register()
