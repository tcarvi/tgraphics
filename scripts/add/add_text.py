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
class ADD_text():
    """Add text"""

    # Class execution
    def execute():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(ADD_text)


# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_text)


# Register
if __name__ == "__main__":
    register()
