# <pep8-80 compliant>
import bpy
import mathutils
from mathutils import Vector


def center_entry_point():
    bpy.context.scene.cursor.rotation_mode = 'XYZ'
    bpy.context.scene.cursor.location = Vector((0.0, 0.0, 0.0))
    bpy.context.scene.cursor.rotation_euler = Vector((0.0, 0.0, 0.0))


def increment_position_entry_point(x_plus, y_plus, z_plus):
    bpy.context.scene.cursor.location[0] += x_plus
    bpy.context.scene.cursor.location[1] += y_plus
    bpy.context.scene.cursor.location[2] += z_plus


def increment_rot_euler_entry_point(x_rot_plus, y_rot_plus, z_rot_plus):
    bpy.context.scene.cursor.rotation_euler[0] += x_rot_plus
    bpy.context.scene.cursor.rotation_euler[1] += y_rot_plus
    bpy.context.scene.cursor.rotation_euler[2] += z_rot_plus


# Class
class MoveEntryPoint():
    """Move entry point"""

    def centralizar():
        center_entry_point()
        return {'FINISHED'}

    def mover(x_plus, y_plus, z_plus):
        increment_position_entry_point(x_plus, y_plus, z_plus)
        return {'FINISHED'}

    def rotacionar(x_rot_plus, y_rot_plus, z_rot_plus):
        increment_rot_euler_entry_point(x_rot_plus, y_rot_plus, z_rot_plus)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(MoveEntryPoint)


def unregister():
    bpy.utils.unregister_class(MoveEntryPoint)


if __name__ == "__main__":
    register()
