import bpy


# Internal method execution
def add_object():

    # TODO - To define input
    # TODO - To add
    print("TODO")


# Class
class ADD_collectionsinstance():
    """ADD collectioninstance"""

    # Class execution
    def execute():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(ADD_collectionsinstance)


# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_collectionsinstance)


# Register
if __name__ == "__main__":
    register()
