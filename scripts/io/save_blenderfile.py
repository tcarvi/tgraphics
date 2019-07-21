import bpy


# Internal method execution
def save_blenderfile(userfilepath):

    # TODO - To define input
    # TODO - To add
    bpy.ops.wm.save_as_mainfile(filepath=userfilepath)


# Class
class SAVE_blenderfile():
    """SAVE_blenderfile"""

    # Class execution
    def execute(userfilepath):
        save_blenderfile(userfilepath)
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
