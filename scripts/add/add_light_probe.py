# <pep8-80 compliant>
import bpy


# Internal method execution
def add_object():
    # TODO - To define input
    t_location_input = 2.0, 2.0, 5.0
    # TODO - To add


# Class
class AddLightProbe():
    """ADD lightprobe with input location"""

    # Class execution
    def add():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(AddLightProbe)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddLightProbe)


# Register
if __name__ == "__main__":
    register()
