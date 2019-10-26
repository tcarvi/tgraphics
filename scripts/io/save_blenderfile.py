import bpy
import os


def save_blenderfile(blenderfilename):
    save_dir = os.path.join(
        os.path.abspath("."),
        "blender_projects"
    )
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    save_path = os.path.join(
        os.path.abspath("."),
        "blender_projects\\" + blenderfilename
    )
    bpy.ops.wm.save_as_mainfile(filepath=save_path)


# Class
class SAVE_blenderfile():
    """SAVE_blenderfile"""

    # Class execution
    def execute(blenderfilename):
        save_blenderfile(blenderfilename)
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(SAVE_blenderfile)


# To unregister
def unregister():
    bpy.utils.unregister_class(SAVE_blenderfile)


# Register
if __name__ == "__main__":
    register()
