# <pep8-80 compliant>
import bpy


# Class
class AddCollectionsInstance:
    """ADD collectioninstance"""

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
    bpy.utils.register_class(AddCollectionsInstance)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddCollectionsInstance)


# Register
if __name__ == "__main__":
    register()
