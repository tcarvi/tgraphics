import bpy

# Internal method execution
def add_light_with_location():

    # TODO - To define input
    locationInput = 2.0, 2.0, 5.0

    light_data = bpy.data.lights.new("MyLightData", 'POINT')
    light_object = bpy.data.objects.new(name="MyLightObject", object_data=light_data)
    bpy.context.scene.collection.objects.link(light_object)
    light_object.location = locationInput

# Class
class ADD_light_with_location():
    """ADD light with input location"""

    # Class execution
    def execute():
        print("Adding light ...")
        add_light_with_location()
        print("Light added")

        return {'FINISHED'}

# To register
def register():
    bpy.utils.register_class(ADD_light_with_location)

# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_light_with_location)

# Register
if __name__ == "__main__":
    register()