# <pep8-80 compliant>
import bpy


# Class
class AddSpeaker():
    """ADD speaker with input location"""

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
    bpy.utils.register_class(AddSpeaker)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddSpeaker)


# Register
if __name__ == "__main__":
    register()
