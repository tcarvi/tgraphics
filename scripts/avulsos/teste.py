import sys
import json

# non-public method
def _update_path_to_unix(windows_path):
    windows_path = windows_path.replace('C:', '')
    windows_path = windows_path.replace('\\', '/')
    return windows_path

# non-public method
def _dir_src_input_data():
    t_dir_src_input_data = \
        "C:\\libs\\python\\src\\github.com\\tgraphics\\input_data"
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        t_dir_src_input_data = _update_path_to_unix(t_dir_src_input_data)
    if t_dir_src_input_data not in sys.path:
        sys.path.append(t_dir_src_input_data)

_dir_src_input_data()
from comando_desenho import EnumComandoDesenho

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
print(type(t_structure))
print(t_structure)