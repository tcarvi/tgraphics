import bpy


# Internal method execution
def add_object():

    # TODO - To define input
    locationInput = 0.0, 0.0, 10.0

    data = bpy.data.cameras.new("camData")
    object = bpy.data.objects.new(name="camObject", object_data=data)
    object.location = locationInput
    bpy.context.scene.collection.objects.link(object)
    # set the active camera
    bpy.context.scene.camera = object


# Class
class ADD_camera():
    """ADD camera with input location"""

    # Class execution
    def execute():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(ADD_camera)


# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_camera)


# Register
if __name__ == "__main__":
    register()
