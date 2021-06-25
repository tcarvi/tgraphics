# <pep8-80 compliant>
import sys


def updatePathToUnixFormat(windowsPath):
    windowsPath = windowsPath.replace('C:', '')
    windowsPath = windowsPath.replace('\\', '/')
    return windowsPath


t_dir_src_add = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\add'
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_dir_src_add = updatePathToUnixFormat(t_dir_src_add)
if t_dir_src_add not in sys.path:
    sys.path.append(t_dir_src_add)

t_dir_src_evaluate = \
    "C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\evaluate"
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_dir_src_evaluate = updatePathToUnixFormat(t_dir_src_evaluate)
if t_dir_src_evaluate not in sys.path:
    sys.path.append(t_dir_src_evaluate)

t_dir_src_io = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\io'
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_dir_src_io = updatePathToUnixFormat(t_dir_src_io)
if t_dir_src_io not in sys.path:
    sys.path.append(t_dir_src_io)

t_dir_src_list = \
    "C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\list"
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_dir_src_list = updatePathToUnixFormat(t_dir_src_list)
if t_dir_src_list not in sys.path:
    sys.path.append(t_dir_src_list)

t_dir_src_move = \
    "C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\move"
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_dir_src_move = updatePathToUnixFormat(t_dir_src_move)
if t_dir_src_move not in sys.path:
    sys.path.append(t_dir_src_move)

t_dir_src_input_data = \
    "C:\\libs\\python\\src\\github.com\\tgraphics\\input_data"
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_dir_src_input_data = updatePathToUnixFormat(t_dir_src_input_data)
if t_dir_src_input_data not in sys.path:
    sys.path.append(t_dir_src_input_data)
