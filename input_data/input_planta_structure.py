# <pep8-80 compliant>
import sys
import json
from comando_desenho import ComandoDesenho


def update_path_to_unix(windows_path):
    windows_path = windows_path.replace('C:', '')
    windows_path = windows_path.replace('\\', '/')
    return windows_path


t_diretorio_input_planta = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\input_data'
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_diretorio_input_planta = update_path_to_unix(t_diretorio_input_planta)
with open('C:\\libs\\python\\src\\github.com\\tgraphics\\input_data\\input_planta_structure.json') as json_data_file:
    t_json_structure = json.load(json_data_file)
    global t_structure
    t_structure = []
    for obj in t_json_structure["comandos"]:
        t_structure.append(
            [
                ComandoDesenho[obj["comando"]].value,
                float(obj["deslocamento"]),
                float(obj["angulo"])
            ]
        )
