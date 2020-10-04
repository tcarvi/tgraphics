# <pep8-80 compliant>
import bpy


# Internal method execution
def add_material(t_object, t_material_name):
    # Get material
    t_material = bpy.data.materials.get(t_material_name)
    print("material0 =")
    print(t_material)
    if t_material is None:
        # create and define material
        t_material = bpy.data.materials.new(name=t_material_name)
        t_material.diffuse_color = (0.8, 0.0503067, 0.0475967, 1)
        print("material1 =")
        print(t_material)
        if t_material_name == "MaterialParedeBranca":
            print("material2 =")
            print(t_material)
    # Assign it to object
    if t_object.data.materials:
        # assign to 1st material slot
        t_object.data.materials[0] = t_material
    else:
        # no slots
        t_object.data.materials.append(t_material)


# Class
class AddMaterial():
    """Add material to an object"""

    # Class execution
    def add(t_object, t_material_name):
        add_material(t_object, t_material_name)
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(AddMaterial)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddMaterial)


# Register
if __name__ == "__main__":
    register()
