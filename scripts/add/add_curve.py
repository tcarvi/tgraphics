# <pep8-80 compliant>
import bpy


# Class
class AddCurve:
    """Create a new Curve Object from data:"""

    # Class execution
    @classmethod
    def add(cls) -> str:
        _add_object()
        return {'FINISHED'}


# non-public method
def _add_object():
    t_data = bpy.data.curves.new(name="curveData", type="CURVE")
    t_object = bpy.data.objects.new(name="curveObject", object_data=t_data)
    bpy.context.scene.collection.objects.link(t_object)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)


# To register
def register():
    bpy.utils.register_class(AddCurve)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddCurve)


# Register
if __name__ == "__main__":
    register()
