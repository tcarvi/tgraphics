# <pep8-80 compliant>
import bpy


def list_objects():

    # print all objects
    for obj in bpy.data.objects:
        print()
        print(obj.name)
        print(obj.name_full)
        print()


# Class
class ListObjects():
    """List all data objects"""

    # Class execution
    def list():
        list_objects()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(ListObjects)


# To unregister
def unregister():
    bpy.utils.unregister_class(ListObjects)


# Register
if __name__ == "__main__":
    register()
