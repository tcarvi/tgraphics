# <pep8-80 compliant>
import bpy


# Internal method execution
def add_object():
    data = bpy.data.curves.new(name="curveData", type="CURVE")
    object = bpy.data.objects.new(name="curveObject", object_data=data)
    bpy.context.scene.collection.objects.link(object)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)


# Class
class AddCurve():
    """Create a new Curve Object from data: """

    # Class execution
    def add():
        add_object()
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(AddCurve)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddCurve)


# Register
if __name__ == "__main__":
    register()
