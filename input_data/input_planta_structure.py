# <pep8-80 compliant>
import sys
import json

def updatePathToUnixFormat(windowsPath):
    windowsPath = windowsPath.replace('C:','')
    windowsPath = windowsPath.replace('\\','/')
    return windowsPath

t_diretorio_input_planta = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\input_data'
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_diretorio_input_planta = updatePathToUnixFormat(t_diretorio_input_planta)

with open('C:\\libs\\python\\src\\github.com\\tgraphics\\input_data\\input_planta_structure.json') as json_data_file:
    global t_structure
    t_structure = json.load(json_data_file)
    # print(t_structure)

#!/usr/bin/env python
# structure = [
#   [
#       tipoDoComandoParaDesenho,
#       deslocamento-comprimento
#       sentido
#   ],
#   ...
# ]
# tipoDoComandoParaDesenho:
#
#     0 Deslocamento ortogonal em X
#     1 Deslocamento ortogonal em Y
#     2 Deslocamento ortogonal em Z
#
#     10 Deslocamento inclinado em X
#     11 Deslocamento inclinado em Y
#     12 Deslocamento inclinado em Z
#
#     20 Retângulo ortogonal de 0.15 em X
#     21 Retângulo ortogonal de 0.15 em Y
#
#     30 Retângulo inclinado de 0.15 em X
#     31 Retângulo inclinado de 0.15 em Y
# A <class 'list'> named structure
# [[30, 8.8], [10, 3.0], [30, 8.3], [21, 22.9], [20, -20.0], [1, -3.0], [21, -21.85]]

# // last
# t_structure = [
#     [
#         30,
#         8.80,
#         6.0
#     ],
#     [
#         10,
#         3.00,
#         6.0
#     ],
#     [
#         30,
#         8.30,
#         6.0
#     ],
#     [
#         21,
#         22.90
#     ],
#     [
#         20,
#         -20.00
#     ],
#     [
#         1,
#         -3.00
#     ],
#     [
#         21,
#         - 21.85
#     ]
# ]
