# <pep8-80 compliant>
import bpy


# Class
class ListScenes():
    """List all data scenes"""

    # Class execution
    def list():
        list_scenes()
        return {'FINISHED'}


def list_scenes():
    # print all scenes
    for t_scene in bpy.data.scenes:
        print("Name = ", t_scene.name)


# To register
def register():
    bpy.utils.register_class(ListScenes)


# To unregister
def unregister():
    bpy.utils.unregister_class(ListScenes)


# Register
if __name__ == "__main__":
    register()
