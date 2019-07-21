import bpy


# Internal method execution
def save_rendering(userfilepath):

    # TODO - To define input
    # TODO - To add
    render = bpy.context.scene.render
    render.use_file_extension = True
    render.filepath = userfilepath
    bpy.ops.render.render(write_still=True)


# Class
class SAVE_rendering():
    """SAVE_blenderfile"""

    # Class execution
    def execute(userfilepath):
        save_rendering(userfilepath)
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(SAVE_rendering)


# To unregister
def unregister():
    bpy.utils.unregister_class(SAVE_rendering)


# Register
if __name__ == "__main__":
    register()
