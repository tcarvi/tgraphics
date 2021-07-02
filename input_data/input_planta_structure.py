# <pep8-80 compliant>
import sys
import json
from comando_desenho import EnumComandoDesenho


# Class
class InputPlantaStruture:
    """Add paths for the program"""

    # Class execution
    @classmethod
    def receive(cls) -> list:
        t_diretorio_input_planta = 'C:\\libs\\python\\src\\github.com\\tgraphics\\input_data'
        if(sys.platform.startswith('linux') or sys.platform.startswith('darwin')):
            t_diretorio_input_planta = _update_path_to_unix(t_diretorio_input_planta)
        t_structure = []
        with open('C:\\libs\\python\\src\\github.com\\tgraphics\\input_data\\input_planta_structure.json') as json_data_file:
            t_json_structure = json.load(json_data_file)
            for obj in t_json_structure["comandos"]:
                t_structure.append(
                    [
                        EnumComandoDesenho[obj["comando"]].value,
                        float(obj["deslocamento"]),
                        float(obj["angulo"])
                    ]
                )
        return t_structure


# non-public method
def _update_path_to_unix(windows_path):
    windows_path = windows_path.replace('C:', '')
    windows_path = windows_path.replace('\\', '/')
    return windows_path


# To register
def register():
    bpy.utils.register_class(InputPlantaStruture)


# To unregister
def unregister():
    bpy.utils.unregister_class(InputPlantaStruture)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
