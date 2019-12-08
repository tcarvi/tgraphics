# <pep8-80 compliant>
import bpy


# Internal method execution
def add_object():
    # TODO - To define input
    locationInput = 0.0, 0.0, 10.0
    data = bpy.data.cameras.new("camData")
    object = bpy.data.objects.new(name="camObject", object_data=data)
    bpy.context.scene.collection.objects.link(object)
    bpy.context.scene.camera = object  # set the active camera
    # OR
    # scene = bpy.context.scene
    # scene.collection.objects.link(object)
    # scene.camera = object
    object.location = locationInput


# Class
class AddCamera():
    """ADD camera with input location"""

    # Class execution
    def add():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(AddCamera)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddCamera)


# Register
if __name__ == "__main__":
    register()
