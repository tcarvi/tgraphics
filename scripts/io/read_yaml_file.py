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
        _read_yaml_file("inputPlantaBaixa.yaml")
        return {'FINISHED'}


# non-public method
def _read_yaml_file(yaml_file_name):
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


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
