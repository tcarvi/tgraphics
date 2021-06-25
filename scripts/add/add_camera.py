# <pep8-80 compliant>
import bpy


# Class
class AddCamera:
    """ADD camera with input location"""

    # Class execution
    @classmethod
    def add(cls, t_location) -> str:
        # print("LOG: Adding camera ...")
        _add_object(t_location)
        # print("LOG: Camera added.")
        return {'FINISHED'}


# non-public method
def _add_object(t_location):
    t_data = bpy.data.cameras.new("camData")
    t_object = bpy.data.objects.new(name="camObject", object_data=t_data)
    bpy.context.scene.collection.objects.link(t_object)
    bpy.context.scene.camera = t_object  # set the active camera
    # OR
    # scene = bpy.context.scene
    # scene.collection.objects.link(object)
    # scene.camera = object
    t_object.location = t_location


# To register
def register():
    bpy.utils.register_class(AddCamera)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddCamera)


# Register
if __name__ == "__main__":
    register()
