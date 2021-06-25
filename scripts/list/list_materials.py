# <pep8-80 compliant>
import bpy


# Class
class ListMaterials():
    """List all data materials"""

    # Class execution
    @classmethod
    def list(cls):
        list_materials()
        return {'FINISHED'}


def list_materials():
    # print all materials
    for t_material in bpy.data.materials:
        print("Name = ", t_material.name)


# To register
def register():
    bpy.utils.register_class(ListMaterials)


# To unregister
def unregister():
    bpy.utils.unregister_class(ListMaterials)


# Register
if __name__ == "__main__":
    register()
