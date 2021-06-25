# <pep8-80 compliant>
import bpy


# Class
class AddForceField:
    """ADD forcefield"""

    # Class execution
    @classmethod
    def add(cls) -> str:
        _add_object()
        return {'FINISHED'}


# non-public method
def _add_object():
    # TODO - To define input
    # TODO - To add
    print("TODO")


# To register
def register():
    bpy.utils.register_class(AddForceField)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddForceField)


# Register
if __name__ == "__main__":
    register()
