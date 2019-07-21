import bpy


# Internal method execution
def add_object():

    # TODO - To define input
    # TODO - To add
    print("TODO")


# Class
class ADD_speaker():
    """ADD speaker with input location"""

    # Class execution
    def execute():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(ADD_speaker)


# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_speaker)


# Register
if __name__ == "__main__":
    register()
