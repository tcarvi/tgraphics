import yaml
import io

# Read YAML file
def read_yamlfile(yamlfilename):

    with open(yamlfilename, 'r') as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)

# Class
class READ_yamlfile():
    """READ_yamlfile"""

    # Class execution
    def execute():
        read_yamlfile("inputPlantaBaixa.yaml")
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(READ_yamlfile)


# To unregister
def unregister():
    bpy.utils.unregister_class(READ_yamlfile)


# Register
if __name__ == "__main__":
    register()