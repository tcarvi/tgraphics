# <pep8-80 compliant>
import bpy


# Class
class ListObjects:
    """List all data objects"""

    # Class execution
    @classmethod
    def list(cls) -> str:
        _list_objects()
        return {'FINISHED'}


def _list_objects():
    # print all objects
    for t_object in bpy.data.objects:
        print("Name = ", t_object.name)


# To register
def register():
    bpy.utils.register_class(ListObjects)


# To unregister
def unregister():
    bpy.utils.unregister_class(ListObjects)


# Register
if __name__ == "__main__":
    register()
