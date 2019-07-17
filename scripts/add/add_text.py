import bpy

# Internal method execution
def add_text_from_data():

    # TODO - To define input
    text = 'Text input'

    txt_data = bpy.data.curves.new(name="MyTextData", type='FONT')
    txt_object = bpy.data.objects.new(name="MyTextObject", object_data=txt_data)
    bpy.context.scene.collection.objects.link(txt_object)   # add the data to the scene as an object
    txt_data.body = text         # the body text to the command line arg given
    txt_data.align_x = 'CENTER'  # center text

# Class
class ADD_text_from_data():
    """Add text"""

    # Class execution
    def execute():
        print("Adding text ...")
        add_text_from_data()
        print("Text added")

        return {'FINISHED'}

# To register
def register():
    bpy.utils.register_class(ADD_text_from_data)

# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_text_from_data)

# Register
if __name__ == "__main__":
    register()