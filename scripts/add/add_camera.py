import bpy

# Internal method execution
def add_camera_with_location():

    # TODO - To define input
    locationInput = 0.0, 0.0, 10.0

    cam_data = bpy.data.cameras.new("MyCamData")
    cam_object = bpy.data.objects.new(name="MyCamObject", object_data=cam_data)
    bpy.context.scene.collection.objects.link(cam_object)  # instance the camera object in the scene
    bpy.context.scene.camera = cam_object       # set the active camera
    cam_object.location = locationInput

# Class
class ADD_camera_with_location():
    """ADD camera with input location"""

    # Class execution
    def execute():
        print("Adding camera ...")
        add_camera_with_location()
        print("Camera added")

        return {'FINISHED'}

# To register
def register():
    bpy.utils.register_class(ADD_camera_with_location)

# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_camera_with_location)

# Register
if __name__ == "__main__":
    register()