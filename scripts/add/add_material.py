# <pep8-80 compliant>
import bpy


# Internal method execution
def add_material(object, material_name):
    # Get material
    material = bpy.data.materials.get(material_name)
    print("material0 =")
    print(material)
    if material is None:
        # create and define material
        material = bpy.data.materials.new(name=material_name)
        material.diffuse_color = (0.8, 0.0503067, 0.0475967, 1)
        print("material1 =")
        print(material)
        if material_name == "MaterialParedeBranca":
            print("material2 =")
            print(material)
    # Assign it to object
    if object.data.materials:
        # assign to 1st material slot
        object.data.materials[0] = material
    else:
        # no slots
        object.data.materials.append(material)


# Class
class AddMaterial():
    """Add material to an object"""

    # Class execution
    def add(object, material_name):
        add_material(object, material_name)
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
