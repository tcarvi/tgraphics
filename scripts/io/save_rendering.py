import bpy
import os


def save_rendering(rendering_file_name):

    save_dir = os.path.join(
        os.path.abspath("."),
        "render_output"
    )
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    save_path = os.path.join(
        os.path.abspath("."),
        "render_output\\" + rendering_file_name
    )
    # TODO - To define input
    # TODO - To add
    render = bpy.context.scene.render
    render.use_file_extension = True
    render.filepath = save_path
    bpy.ops.render.render(write_still=True)

# Class
class SaveRendering():
    """Save rendering file"""

    # Class execution
    def execute(rendering_file_name):
        save_rendering(rendering_file_name)
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(SaveRendering)


# To unregister
def unregister():
    bpy.utils.unregister_class(SaveRendering)


# Register
if __name__ == "__main__":
    register()
