import bpy


# Internal method execution
def add_object():

    # TODO - To define input
    # TODO - To add
    print("TODO")


# Class
class AddLattice():
    """ADD lattice with input location"""

    # Class execution
    def add():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(AddLattice)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddLattice)


# Register
if __name__ == "__main__":
    register()
