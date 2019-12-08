# <pep8-80 compliant>
import bpy


# Internal method execution
def add_object():
    # TODO - To define input
    t_location_input = 0.0, 0.0, 10.0
    t_data = bpy.data.cameras.new("camData")
    t_object = bpy.data.objects.new(name="camObject", object_data=t_data)
    bpy.context.scene.collection.objects.link(t_object)
    bpy.context.scene.camera = t_object  # set the active camera
    # OR
    # scene = bpy.context.scene
    # scene.collection.objects.link(object)
    # scene.camera = object
    t_object.location = t_location_input


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
