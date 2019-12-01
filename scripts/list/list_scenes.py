# <pep8-80 compliant>
import bpy


def list_scenes():

    # print all scene names in a list
        print(bpy.data.scenes.keys())


# Class
class ListScenes():
    """List all data scenes"""

    # Class execution
    def list():
        list_scenes()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(ListScenes)


# To unregister
def unregister():
    bpy.utils.unregister_class(ListScenes)


# Register
if __name__ == "__main__":
    register()