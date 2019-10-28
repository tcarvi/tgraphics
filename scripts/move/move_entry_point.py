import bpy

def center_entry_point():
    bpy.context.scene.cursor.rotation_mode = 'XYZ'
    bpy.context.scene.cursor.location[0] = 0.00
    bpy.context.scene.cursor.location[1] = 0.00
    bpy.context.scene.cursor.location[2] = 0.00
    bpy.context.scene.cursor.rotation_euler[0] = 0.00
    bpy.context.scene.cursor.rotation_euler[1] = 0.00
    bpy.context.scene.cursor.rotation_euler[2] = 0.00
    bpy.context.view_layer.update()

def increment_position_entry_point(x_plus, y_plus, z_plus):
    bpy.context.scene.cursor.location[0] += x_plus
    bpy.context.scene.cursor.location[1] += y_plus
    bpy.context.scene.cursor.location[2] += z_plus
    bpy.context.view_layer.update()

def increment_rotation_euler_entry_point(x_rotation_euler_plus, y_rotation_euler_plus, z_rotation_euler_plus):
    bpy.context.scene.cursor.rotation_euler[0] += x_rotation_euler_plus
    bpy.context.scene.cursor.rotation_euler[1] += y_rotation_euler_plus
    bpy.context.scene.cursor.rotation_euler[2] += z_rotation_euler_plus
    bpy.context.view_layer.update()


# Class
class MoveEntryPoint():
    """Move entry point"""

    def centralizar():
        center_entry_point()
        return {'FINISHED'}
    
    def mover(x_plus, y_plus, z_plus):
        increment_position_entry_point(x_plus, y_plus, z_plus)
        return {'FINISHED'}
    
    def rotacionar(x_rotation_euler_plus, y_rotation_euler_plus, z_rotation_euler_plus):
        increment_rotation_euler_entry_point(x_rotation_euler_plus, y_rotation_euler_plus, z_rotation_euler_plus)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MoveEntryPoint)


def unregister():
    bpy.utils.unregister_class(MoveEntryPoint)


if __name__ == "__main__":
    register()
