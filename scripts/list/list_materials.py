# <pep8-80 compliant>
import bpy


def list_materials():

    # print all materials
    for material in bpy.data.materials:
        print("Name = ", material.name)


# Class
class ListMaterials():
    """List all data materials"""

    # Class execution
    def list():
        list_materials()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(ListMaterials)


# To unregister
def unregister():
    bpy.utils.unregister_class(ListMaterials)


# Register
if __name__ == "__main__":
    register()
