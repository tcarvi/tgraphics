# <pep8-80 compliant>
import sys

def updatePathToUnixFormat(windowsPath):
    windowsPath = windowsPath.replace('C:','')
    windowsPath = windowsPath.replace('\\','/')
    return windowsPath

t_diretorio_scripts_add = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\add'
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_diretorio_scripts_add = updatePathToUnixFormat(t_diretorio_scripts_add)
if t_diretorio_scripts_add not in sys.path:
    sys.path.append(t_diretorio_scripts_add)

t_diretorio_scripts_io = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\io'
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_diretorio_scripts_io = updatePathToUnixFormat(t_diretorio_scripts_io)
if t_diretorio_scripts_io not in sys.path:
    sys.path.append(t_diretorio_scripts_io)

t_diretorio_scripts_move = \
    "C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\move"
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_diretorio_scripts_move = updatePathToUnixFormat(t_diretorio_scripts_move)
if t_diretorio_scripts_move not in sys.path:
    sys.path.append(t_diretorio_scripts_move)

t_diretorio_scripts_list = \
    "C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\list"
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_diretorio_scripts_list = updatePathToUnixFormat(t_diretorio_scripts_list)
if t_diretorio_scripts_list not in sys.path:
    sys.path.append(t_diretorio_scripts_list)

t_diretorio_scripts_evaluate = \
    "C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\evaluate"
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_diretorio_scripts_evaluate = updatePathToUnixFormat(t_diretorio_scripts_evaluate)
if t_diretorio_scripts_evaluate not in sys.path:
    sys.path.append(t_diretorio_scripts_evaluate)

t_diretorio_input_data = \
    "C:\\libs\\python\\src\\github.com\\tgraphics\\input_data"
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_diretorio_input_data = updatePathToUnixFormat(t_diretorio_input_data)
if t_diretorio_input_data not in sys.path:
    sys.path.append(t_diretorio_input_data)
