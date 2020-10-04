# <pep8-80 compliant>
import sys

def updatePathToUnixFormat(windowsPath):
    windowsPath = windowsPath.replace('C:','')
    windowsPath = windowsPath.replace('\\','/')
    return windowsPath

diretorio_scripts_add = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\add'
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    diretorio_scripts_add = updatePathToUnixFormat(diretorio_scripts_add)
if diretorio_scripts_add not in sys.path:
    sys.path.append(diretorio_scripts_add)

diretorio_scripts_io = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\io'
if sys.platform.startswith('linux') or sys.platform.startswith('mac'):
    diretorio_scripts_io = updatePathToUnixFormat(diretorio_scripts_io)
if diretorio_scripts_io not in sys.path:
    sys.path.append(diretorio_scripts_io)

diretorio_scripts_move = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\move'
if sys.platform.startswith('linux') or sys.platform.startswith('mac'):
    diretorio_scripts_move = updatePathToUnixFormat(diretorio_scripts_move)
if diretorio_scripts_move not in sys.path:
    sys.path.append(diretorio_scripts_move)

diretorio_scripts_list = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\list'
if sys.platform.startswith('linux') or sys.platform.startswith('mac'):
    diretorio_scripts_list = updatePathToUnixFormat(diretorio_scripts_list)
if diretorio_scripts_list not in sys.path:
    sys.path.append(diretorio_scripts_list)

diretorio_scripts_evaluate = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\evaluate'
if sys.platform.startswith('linux') or sys.platform.startswith('mac'):
    diretorio_scripts_evaluate = updatePathToUnixFormat(diretorio_scripts_evaluate)
if diretorio_scripts_evaluate not in sys.path:
    sys.path.append(diretorio_scripts_evaluate)

diretorio_input_data = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\input_data'
if sys.platform.startswith('linux') or sys.platform.startswith('mac'):
    diretorio_input_data = updatePathToUnixFormat(diretorio_input_data)
if diretorio_input_data not in sys.path:
    sys.path.append(diretorio_input_data)