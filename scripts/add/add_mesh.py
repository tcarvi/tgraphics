#!/usr/bin/env python3
import bpy
from mathutils import Vector, Matrix
from move_entry_point import MoveEntryPoint
import json
from math import radians


def processar_estrutura(structure):

    # with open('C:\\libs\\python\\src\\github.com\\tgraphics\\input_data\\input_planta_structure.json') as json_data_file:
    #     data = json.load(json_data_file)
    #     print(data)

    # MoveEntryPoint.centralizar()

    for d in structure:
        if d[0] < 10:
            if d[0] == 0:
                # Atualiza posição X
                bpy.context.scene.cursor.location[0] += d[1]
                bpy.context.view_layer.update()
                continue
            if d[0] == 1:
                # Atualiza posição Y
                bpy.context.scene.cursor.location[1] += d[1]
                bpy.context.view_layer.update()
                continue
            if d[0] == 2:
                # Atualiza posição Z
                bpy.context.scene.cursor.location[2] += d[1]
                bpy.context.view_layer.update()
                continue
            if d[0] == 3:
                # Atualiza posição XY
                bpy.context.scene.cursor.location[0] += d[1]
                bpy.context.scene.cursor.location[1] += d[2]
                bpy.context.view_layer.update()
                continue
            continue
        if d[0] < 20:
            if d[0] == 10:
                # Atualiza rotação do eixo X
                bpy.context.scene.cursor.rotation_euler[0] += radians(d[1])
                bpy.context.view_layer.update()
                continue
            if d[0] == 11:
                # Atualiza rotação do eixo Y
                bpy.context.scene.cursor.rotation_euler[1] += radians(d[1])
                bpy.context.view_layer.update()
                continue
            if d[0] == 12:
                # Atualiza rotação do eixo Z
                bpy.context.scene.cursor.rotation_euler[2] += radians(d[1])
                bpy.context.view_layer.update()
                continue
            if d[0] == 13:
                # Atualiza rotação do plano XY no mesmo ângulo
                bpy.context.scene.cursor.rotation_euler[0] += radians(d[1])
                bpy.context.scene.cursor.rotation_euler[1] += radians(d[1])
                bpy.context.view_layer.update()
                continue
            continue
        if d[0] < 30:
            if d[0] == 20:
                # Desenha parede de 0.15 metros de largura, no eixo X  OK
                print("add_parede_15_centimetros_horizontal")
                add_parede_15_centimetros_horizontal(d[1])
                bpy.context.scene.cursor.location[0] += d[1]
                bpy.context.view_layer.update()
                continue
            if d[0] == 21:
                # Desenha parede de 0.15 metros de largura, no eixo Y
                print("add_parede_15_centimetros_transversal")
                add_parede_15_centimetros_transversal(d[1])
                bpy.context.scene.cursor.location[1] += d[1]
                bpy.context.view_layer.update()
                continue
            continue

    print(bpy.context.scene.cursor.rotation_euler)


# Internal method execution
def add_parede_15_centimetros_horizontal(xValue):
    bpy.context.view_layer.update()
    data = bpy.data.meshes.new(name="meshData")
    espessura_parede = 0.15
    if xValue < 0:
        espessura_parede *= -1
    # Vector1 = (original)
    # Vector1 = (Como original, mas com espessura da parede.)
    data.from_pydata(
        [
            Vector(
                (
                    bpy.context.scene.cursor.location[0],
                    bpy.context.scene.cursor.location[1],
                    bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    bpy.context.scene.cursor.location[0] + xValue,
                    bpy.context.scene.cursor.location[1],
                    bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    bpy.context.scene.cursor.location[0] + xValue,
                    bpy.context.scene.cursor.location[1] + espessura_parede,
                    bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    bpy.context.scene.cursor.location[0],
                    bpy.context.scene.cursor.location[1] + espessura_parede,
                    bpy.context.scene.cursor.location[2]
                )
            )
        ],
        [
            []
        ],
        [
            [0, 1, 2, 3]
        ]
    )
    object = bpy.data.objects.new(
        name="meshObject",
        object_data=data
    )
    bpy.context.scene.collection.objects.link(object)

# Internal method execution
def add_parede_15_centimetros_transversal(yValue):
    medida_parede = 0.15
    if yValue > 0:
        medida_parede *= -1
    bpy.context.view_layer.update()
    data = bpy.data.meshes.new(name="meshData")
    data.from_pydata(
        [
            
            Vector(
                    (
                        bpy.context.scene.cursor.location[0],
                        bpy.context.scene.cursor.location[1],
                        bpy.context.scene.cursor.location[2]
                    )
            ),
            Vector(
                    (
                        bpy.context.scene.cursor.location[0],
                        bpy.context.scene.cursor.location[1] + yValue,
                        bpy.context.scene.cursor.location[2]
                    )
            ),
            Vector(
                    (
                        bpy.context.scene.cursor.location[0] + medida_parede,
                        bpy.context.scene.cursor.location[1] + yValue,
                        bpy.context.scene.cursor.location[2]
                    )
            ),
            Vector(
                    (
                        bpy.context.scene.cursor.location[0] + medida_parede,
                        bpy.context.scene.cursor.location[1],
                        bpy.context.scene.cursor.location[2]
                    )
            )
        ],
        [
            []
        ],
        [
            [0, 1, 2, 3]
        ]
    )
    object = bpy.data.objects.new(
        name="meshObject",
        object_data=data
    )
    bpy.context.scene.collection.objects.link(object)

    # Internal method execution
# def add_parede_15_centimetros_transversal(yValue):

#     bpy.context.view_layer.update()
#     data = bpy.data.meshes.new(name="meshData")
#     data.from_pydata(
#         [
#             Matrix.Rotation(
#                 Vector(
#                     (
#                         bpy.context.scene.cursor.location[0],
#                         bpy.context.scene.cursor.location[1],
#                         bpy.context.scene.cursor.location[2]
#                     )
#                 )
#             ),
#             Matrix.Rotation(
#                 Vector(
#                     (
#                         bpy.context.scene.cursor.location[0],
#                         bpy.context.scene.cursor.location[1] + yValue,
#                         bpy.context.scene.cursor.location[2]
#                     )
#                 )
#             ),
#             Matrix.Rotation(
#                 Vector(
#                     (
#                         bpy.context.scene.cursor.location[0] - 0.15,
#                         bpy.context.scene.cursor.location[1] + yValue,
#                         bpy.context.scene.cursor.location[2]
#                     )
#             ),
#             Matrix.Rotation(
#                 Vector(
#                     (
#                         bpy.context.scene.cursor.location[0] - 0.15,
#                         bpy.context.scene.cursor.location[1],
#                         bpy.context.scene.cursor.location[2]
#                     )
#                 )
#             )
#         ],
#         [
#             []
#         ],
#         [
#             [0, 1, 2, 3]
#         ]
#     )
#     object = bpy.data.objects.new(
#         name="meshObject",
#         object_data=data
#     )
#     bpy.context.scene.collection.objects.link(object)

#     # Internal method execution
# def add_parede_15_centimetros_transversal(yValue):

#     bpy.context.view_layer.update()
#     data = bpy.data.meshes.new(name="meshData")
#     data.from_pydata(
#         [
#             Matrix.Rotation(
#                 Vector(
#                     (
#                         bpy.context.scene.cursor.location[0],
#                         bpy.context.scene.cursor.location[1],
#                         bpy.context.scene.cursor.location[2]
#                     )
#                 )
#             ),
#             Matrix.Rotation(
#                 Vector(
#                     (
#                         bpy.context.scene.cursor.location[0],
#                         bpy.context.scene.cursor.location[1] + yValue,
#                         bpy.context.scene.cursor.location[2]
#                     )
#                 )
#             ),
#             Matrix.Rotation(
#                 Vector(
#                     (
#                         bpy.context.scene.cursor.location[0] - 0.15,
#                         bpy.context.scene.cursor.location[1] + yValue,
#                         bpy.context.scene.cursor.location[2]
#                     )
#             ),
#             Matrix.Rotation(
#                 Vector(
#                     (
#                         bpy.context.scene.cursor.location[0] - 0.15,
#                         bpy.context.scene.cursor.location[1],
#                         bpy.context.scene.cursor.location[2]
#                     )
#                 )
#             )
#         ],
#         [
#             []
#         ],
#         [
#             [0, 1, 2, 3]
#         ]
#     )
#     object = bpy.data.objects.new(
#         name="meshObject",
#         object_data=data
#     )
#     bpy.context.scene.collection.objects.link(object)

# horiRot = rotMat(theta, 3, 'X')
#                             vertRot = rotMat(phi, 3, 'Z')

#                             basisVecX.rotate(horiRot)
# Class
class AddMesh():
    """Create a new Mesh Object from data: vertices, edges and faces"""

    # Class execution
    def add(structure):
        processar_estrutura(structure)
        return {'FINISHED'}


# To register
def register():
    bpy.utils.register_class(AddMesh)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddMesh)


# Register
if __name__ == "__main__":
    register()
