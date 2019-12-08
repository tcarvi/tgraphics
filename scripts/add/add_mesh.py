# <pep8-80 compliant>
import bpy
from mathutils import Vector, Matrix
from move_entry_point import MoveEntryPoint
import json
from math import radians
from add_material import AddMaterial


def processar_estrutura(structure):
    # with open('C:\\libs\\python\\src\\github.com\\tgraphics\\input_data
    #               \\input_planta_structure.json') as json_data_file:
    #     data = json.load(json_data_file)
    #     print(data)
    # MoveEntryPoint.centralizar()
    for d in structure:
        # Each item "d" is a <class 'list'>
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
        if d[0] < 40:
            if d[0] == 30:
                # Desenha parede de 0.15 metros de largura, no eixo X inclinado
                print("add_parede_15_centimetros_inclinado_em_x")
                add_parede_15_centimetros_inclinado_em_x(d[1])
                bpy.context.scene.cursor.location[0] += d[1]
                bpy.context.view_layer.update()
                continue
            if d[0] == 31:
                # Desenha parede de 0.15 metros de largura, no eixo Y inclinado
                print("add_parede_15_centimetros_inclinado_em_y")
                add_parede_15_centimetros_inclinado_em_x(d[1])
                bpy.context.scene.cursor.location[1] += d[1]
                bpy.context.view_layer.update()
                continue
            continue
    print(bpy.context.scene.cursor.rotation_euler)


def add_parede_15_centimetros_horizontal(x_value):
    espessura_parede = 0.15
    if x_value < 0:
        espessura_parede *= -1
    data = bpy.data.meshes.new(name="meshData")
    # data is a <class 'bpy_types.Mesh'>
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
                    bpy.context.scene.cursor.location[0] + x_value,
                    bpy.context.scene.cursor.location[1],
                    bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    bpy.context.scene.cursor.location[0] + x_value,
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
    # object is a <class 'bpy_types.Object'>
    AddMaterial.add(object, "MaterialParedeBranca")
    bpy.context.scene.collection.objects.link(object)


def add_parede_15_centimetros_transversal(y_value):
    medida_parede = 0.15
    if y_value > 0:
        medida_parede *= -1
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
                        bpy.context.scene.cursor.location[1] + y_value,
                        bpy.context.scene.cursor.location[2]
                    )
            ),
            Vector(
                    (
                        bpy.context.scene.cursor.location[0] + medida_parede,
                        bpy.context.scene.cursor.location[1] + y_value,
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
    AddMaterial.add(object, "MaterialParedeBranca")
    bpy.context.scene.collection.objects.link(object)


def add_parede_15_centimetros_inclinado_em_x(x_value):
    # create a location matrix
    # mat_loc = Matrix.Translation((2.0, 3.0, 4.0))
    # print(mat_loc)
    # create an identitiy matrix
    # mat_sca = Matrix.Scale(0.5, 4, (0.0, 0.0, 1.0))
    # print(mat_sca)
    vec = Vector((1, 2, 3))
    # vec is a <class 'Vector'>
    # create a rotation matrix
    mat_rot = Matrix.Rotation(radians(83.0), 3, 'X')
    # mat_rot is a <class 'Matrix'>
    # combine transformations
    mat_out = mat_rot @ vec
    # mat_out is a <class 'Vector'>
    # espessura_parede = 0.15
    # if xValue < 0:
    #     espessura_parede *= -1
    # # create a rotation matrix
    # mat_rot = mathutils.Matrix.Rotation(radians(83.0), 4, 'X')
    # # create a location matrix
    # mat_loc_ponto_2 = mathutils.Matrix.Translation(
    #     (
    #         bpy.context.scene.cursor.location[0] + xValue,
    #         bpy.context.scene.cursor.location[1],
    #         bpy.context.scene.cursor.location[2]
    # )
    # vetor_ponto_2 =
    # data = bpy.data.meshes.new(name="meshData")
    # data.from_pydata(
    #     [
    #         Matrix.Rotation(
    #             Vector(
    #                 (
    #                     bpy.context.scene.cursor.location[0],
    #                     bpy.context.scene.cursor.location[1],
    #                     bpy.context.scene.cursor.location[2]
    #                 )
    #             )
    #         ),
    #         Matrix.Rotation(
    #             Vector(
    #                 (
    #                     bpy.context.scene.cursor.location[0] + xValue,
    #                     bpy.context.scene.cursor.location[1],
    #                     bpy.context.scene.cursor.location[2]
    #                 )
    #             )
    #         ),
    #         Matrix.Rotation(
    #             Vector(
    #                 (
    #                 bpy.context.scene.cursor.location[0] + xValue,
    #                 bpy.context.scene.cursor.location[1] + espessura_parede,
    #                 bpy.context.scene.cursor.location[2]
    #                 )
    #             )
    #         ),
    #         Matrix.Rotation(
    #             Vector(
    #                 (
    #                bpy.context.scene.cursor.location[0],
    #                bpy.context.scene.cursor.location[1] + espessura_parede,
    #                bpy.context.scene.cursor.location[2]
    #                 )
    #             )
    #         )
    #     ],
    #     [
    #         []
    #     ],
    #     [
    #         [0, 1, 2, 3]
    #     ]
    # )
    # object = bpy.data.objects.new(
    #     name="meshObject",
    #     object_data=data
    # )
    # bpy.context.scene.collection.objects.link(object)

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
