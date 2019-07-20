import bpy

# Internal method execution
def add_object():

    data = bpy.data.curves.new(name="curveData", type="CURVE")
    object = bpy.data.objects.new(name="curveObject", object_data=data)
    bpy.context.scene.collection.objects.link(object)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)

# Class
class ADD_curve_from_data():
    """Create a new Curve Object from data: """

    # Class execution
    def execute():
        add_object()
        return {'FINISHED'}

# To register
def register():
    bpy.utils.register_class(ADD_curve)

# To unregister
def unregister():
    bpy.utils.unregister_class(ADD_curve)

# Register
if __name__ == "__main__":
    register()