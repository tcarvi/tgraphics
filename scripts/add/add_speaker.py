# <pep8-80 compliant>
import bpy


# Class
class AddSpeaker:
    """ADD speaker with input location"""

    # Class execution
    @classmethod
    def add(cls) -> str:
        _add_object()
        return {'FINISHED'}


# Internal method execution
def _add_object() -> None:
    # TODO - To define input
    # TODO - To add
    print("TODO")


# To register
def register():
    bpy.utils.register_class(AddSpeaker)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddSpeaker)


# Register
if __name__ == "__main__":
    register()
