# <pep8-80 compliant>
import bpy


# Internal method execution
def add_light(initialPosition):
    data = bpy.data.lights.new("lightData", 'POINT')
    object = bpy.data.objects.new(name="lightObject", object_data=data)
    object.location = initialPosition
    bpy.context.scene.collection.objects.link(object)


# Class
class AddLight():
    """ADD light with input location"""

    # Class execution
    def add(initialPosition):
        add_light(initialPosition)
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(AddLight)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddLight)


# Register
if __name__ == "__main__":
    register()
