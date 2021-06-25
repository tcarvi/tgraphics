# <pep8-80 compliant>
import bpy
import mathutils


def center_entry_point():
    bpy.context.scene.cursor.rotation_mode = 'XYZ'
    bpy.context.scene.cursor.location = Vector((0.0, 0.0, 0.0))
    bpy.context.scene.cursor.rotation_euler = Vector((0.0, 0.0, 0.0))


def increment_position_entry_point(t_plus_x, t_plus_y, t_plus_z):
    bpy.context.scene.cursor.location[0] += t_plus_x
    bpy.context.scene.cursor.location[1] += t_plus_y
    bpy.context.scene.cursor.location[2] += t_plus_z


def increment_rot_euler_entry_point(t_rot_plus_x, t_rot_plus_y, t_rot_plus_z):
    bpy.context.scene.cursor.rotation_euler[0] += t_rot_plus_x
    bpy.context.scene.cursor.rotation_euler[1] += t_rot_plus_y
    bpy.context.scene.cursor.rotation_euler[2] += t_rot_plus_z


# Class
class MoveEntryPoint():
    """Move entry point"""

    def centralizar():
        center_entry_point()
        return {'FINISHED'}

    def mover(t_plus_x, t_plus_y, t_plus_z):
        increment_position_entry_point(
            t_plus_x,
            t_plus_y,
            t_plus_z
            )
        return {'FINISHED'}

    def rotacionar(t_rot_plus_x, t_rot_plus_y, t_rot_plus_z):
        increment_rot_euler_entry_point(
            t_rot_plus_x,
            t_rot_plus_y,
            t_rot_plus_z
            )
        return {'FINISHED'}


def register():
    bpy.utils.register_class(MoveEntryPoint)


def unregister():
    bpy.utils.unregister_class(MoveEntryPoint)


if __name__ == "__main__":
    register()
