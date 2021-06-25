# <pep8-80 compliant>
import bpy


# Class
class AddText():
    """Add text"""

    # Class execution
    def add():
        add_object()
        return {'FINISHED'}


# Internal method execution
def add_object():
    # TODO - To define input
    t_text = 'Text input'
    t_data = bpy.data.curves.new(name="textData", type='FONT')
    t_object = bpy.data.objects.new(name="textObject", object_data=t_data)
    t_data.body = t_text
    t_data.align_x = 'CENTER'
    bpy.context.scene.collection.objects.link(t_object)
    # OR
    # scene = bpy.context.scene
    # scene.collection.objects.link(txt_ob)


# To register
def register():
    bpy.utils.register_class(AddText)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddText)


# Register
if __name__ == "__main__":
    register()
