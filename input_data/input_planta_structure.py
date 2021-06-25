# <pep8-80 compliant>
import sys
import json
from enum import Enum


class ComandoDesenho(Enum):
    DeslocarEmX = 0
    DeslocarEmY = 1
    DeslocarEmZ = 2
    DeslocarEmXInclinado = 10
    DeslocarEmYInclinado = 11
    DeslocarEmZInclinado = 12
    DesenharRetanguloEmX = 20
    DesenharRetanguloEmY = 21
    DesenharRetanguloEmZ = 22
    DesenharRetanguloEmXInclinado = 30
    DesenharRetanguloEmYInclinado = 31
    DesenharRetanguloEmZInclinado = 32


def updatePathToUnixFormat(windowsPath):
    windowsPath = windowsPath.replace('C:', '')
    windowsPath = windowsPath.replace('\\', '/')
    return windowsPath


t_diretorio_input_planta = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\input_data'
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_diretorio_input_planta = updatePathToUnixFormat(t_diretorio_input_planta)

with open('C:\\libs\\python\\src\\github.com\\tgraphics\\input_data\\input_planta_structure.json') as json_data_file:
    t_json_structure = json.load(json_data_file)
    global t_structure
    t_structure = []
    for obj in t_json_structure["comandos"]:
        t_structure.append([ComandoDesenho[obj["comando"]].value, float(obj["deslocamento"]), float(obj["angulo"])])

# !/usr/bin/env python
# structure = [
#   [
#       tipoDoComandoParaDesenho,
#       deslocamento-comprimento
#       angulo
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
#
# // Exemplo depois do processamento:
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
