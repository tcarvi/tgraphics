# <pep8-80 compliant>
import bpy


# Class
class AddEmpty:
    """ADD empty with input location"""

    # Class execution
    @classmethod
    def add(cls) -> str:
        _add_object()
        return {'FINISHED'}


# non-public method
def _add_object() -> None:
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
