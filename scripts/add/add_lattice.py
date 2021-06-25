# <pep8-80 compliant>
import bpy


# Class
class AddLattice:
    """ADD lattice with input location"""

    # Class execution
    @classmethod
    def add(cls):
        _add_object()
        return {'FINISHED'}


# non-public method
def _add_object():
    # TODO - To define input
    # TODO - To add
    print("TODO")


# To register
def register():
    bpy.utils.register_class(AddLattice)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddLattice)


# Register
if __name__ == "__main__":
    register()
