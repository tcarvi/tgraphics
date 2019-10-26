import bpy
import os


def save_rendering(renderingfilename):

    save_dir = os.path.join(
        os.path.abspath("."),
        "render_output"
    )
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    save_path = os.path.join(
        os.path.abspath("."),
        "render_output\\" + renderingfilename
    )
    # TODO - To define input
    # TODO - To add
    render = bpy.context.scene.render
    render.use_file_extension = True
    render.filepath = save_path
    bpy.ops.render.render(write_still=True)

# Class
class SAVE_rendering():
    """SAVE_blenderfile"""

    # Class execution
    def execute(renderingfilename):
        save_rendering(renderingfilename)
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
