# <pep8-80 compliant>
import bpy
import io
import yaml


# Class
class ReadYamlFile:
    """READ yaml file"""

    # Class execution
    @classmethod
    def execute(cls):
        read_yaml_file("inputPlantaBaixa.yaml")
        return {'FINISHED'}


# Read YAML file
def read_yaml_file(yaml_file_name):
    with open(yaml_file_name, 'r') as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)


# To register
def register():
    bpy.utils.register_class(ReadYamlFile)


# To unregister
def unregister():
    bpy.utils.unregister_class(ReadYamlFile)


# Register
if __name__ == "__main__":
    register()
