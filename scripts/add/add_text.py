# <pep8-80 compliant>
import bpy


# Internal method execution
def add_object():

    # TODO - To define input
    text = 'Text input'

    data = bpy.data.curves.new(name="textData", type='FONT')
    object = bpy.data.objects.new(name="textObject", object_data=data)
    data.body = text
    data.align_x = 'CENTER'
    bpy.context.scene.collection.objects.link(object)
    # OR
    # scene = bpy.context.scene
    # scene.collection.objects.link(txt_ob)


# Class
class AddText():
    """Add text"""

    # Class execution
    def add():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(AddText)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddText)


# Register
if __name__ == "__main__":
    register()
