# <pep8-80 compliant>
import bpy
from mathutils import Vector, Matrix
from move_entry_point import MoveEntryPoint
import json
import math
from add_material import AddMaterial


def processar_estrutura(t_structure):
    # with open('C:\\libs\\python\\src\\github.com\\tgraphics\\input_data
    #               \\input_planta_structure.json') as json_data_file:
    #     data = json.load(json_data_file)
    #     print(data)
    # MoveEntryPoint.centralizar()
    print(t_structure)
    # [[30, 8.8], [10, 3.0], [30, 8.3], [21, 22.9], [20, -20.0], [1, -3.0], [21, -21.85]]
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
    # Primeiro comando: 30 -> Retângulo inclinado de 0.15 em X
    #                   No valor de 8.8
    for d in t_structure:
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
                # Desloca com rotação do eixo X
                t_medida_deslocamento = d[1]
                t_inclinação_deslocamento_graus = d[2]
                t_inclinação_deslocamento_radianos = math.radians(t_inclinação_deslocamento_graus)
                bpy.context.scene.cursor.location[0] += t_medida_deslocamento * math.cos(t_inclinação_deslocamento_radianos)
                bpy.context.scene.cursor.location[1] += 0.15 * math.cos(t_inclinação_deslocamento_radianos),
                bpy.context.view_layer.update()
                continue
            if d[0] == 11:
                # TODO
                # Atualiza rotação do eixo Y
                bpy.context.scene.cursor.rotation_euler[1] += math.radians(d[1])
                bpy.context.view_layer.update()
                continue
            if d[0] == 12:
                # TODO
                # Atualiza rotação do eixo Z
                bpy.context.scene.cursor.rotation_euler[2] += math.radians(d[1])
                bpy.context.view_layer.update()
                continue
            if d[0] == 13:
                # TODO
                # Atualiza rotação do plano XY no mesmo ângulo
                bpy.context.scene.cursor.rotation_euler[0] += math.radians(d[1])
                bpy.context.scene.cursor.rotation_euler[1] += math.radians(d[1])
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
                t_medida_parede = d[1]
                t_inclinação_parede_graus = d[2]
                t_inclinação_parede_radianos = math.radians(t_inclinação_parede_graus)
                add_parede_15_centimetros_inclinado_em_x(t_medida_parede)
                bpy.context.scene.cursor.location[0] += t_medida_parede * math.cos(t_inclinação_parede_radianos)
                bpy.context.scene.cursor.location[1] += 0.15 * math.cos(t_inclinação_parede_radianos),
                bpy.context.view_layer.update()
                print("added parede_15_centimetros_inclinado_em_x")
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


def add_parede_15_centimetros_horizontal(t_value_x):
    t_espessura_parede = 0.15
    if t_value_x < 0:
        t_espessura_parede *= -1
    t_data = bpy.data.meshes.new(name="meshData")
    # data is a <class 'bpy_types.Mesh'>
    t_data.from_pydata(
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
                    bpy.context.scene.cursor.location[0] + t_value_x,
                    bpy.context.scene.cursor.location[1],
                    bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    bpy.context.scene.cursor.location[0] + t_value_x,
                    bpy.context.scene.cursor.location[1] + t_espessura_parede,
                    bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    bpy.context.scene.cursor.location[0],
                    bpy.context.scene.cursor.location[1] + t_espessura_parede,
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
    t_object = bpy.data.objects.new(
        name="meshObject",
        object_data=t_data
    )
    verts = len(t_data.vertices)
    print("verts HORIZONTAL = ")
    print(verts)
    print("verts0 = ")
    print(t_data.vertices[0].co)
    print("verts1 = ")
    print(t_data.vertices[1].co)
    print("verts2 = ")
    print(t_data.vertices[2].co)
    print("verts3 = ")
    print(t_data.vertices[3].co)

    AddMaterial.add(t_object, "MaterialParedeBranca")
    bpy.context.scene.collection.objects.link(t_object)


def add_parede_15_centimetros_transversal(t_value_y):
    t_medida_parede = 0.15
    if t_value_y > 0:
        t_medida_parede *= -1
    t_data = bpy.data.meshes.new(name="meshData")
    t_data.from_pydata(
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
                        bpy.context.scene.cursor.location[1] + t_value_y,
                        bpy.context.scene.cursor.location[2]
                    )
            ),
            Vector(
                    (
                        bpy.context.scene.cursor.location[0] + t_medida_parede,
                        bpy.context.scene.cursor.location[1] + t_value_y,
                        bpy.context.scene.cursor.location[2]
                    )
            ),
            Vector(
                    (
                        bpy.context.scene.cursor.location[0] + t_medida_parede,
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
    t_object = bpy.data.objects.new(
        name="meshObject",
        object_data=t_data
    )

    verts = len(t_data.vertices)
    print("verts TRANSVERSAL = ")
    print(verts)
    print("verts0 = ")
    print(t_data.vertices[0].co)
    print("verts1 = ")
    print(t_data.vertices[1].co)
    print("verts2 = ")
    print(t_data.vertices[2].co)
    print("verts3 = ")
    print(t_data.vertices[3].co)

    AddMaterial.add(t_object, "MaterialParedeBranca")
    bpy.context.scene.collection.objects.link(t_object)


def add_parede_15_centimetros_inclinado_em_x(t_value_x):
    # create a location matrix
    # mat_loc = Matrix.Translation((2.0, 3.0, 4.0))
    # print(mat_loc)
    # create an identitiy matrix
    # mat_sca = Matrix.Scale(0.5, 4, (0.0, 0.0, 1.0))
    # print(mat_sca)
    # """ t_vec = Vector((1, 2, 3))
    # print("t_vec =")
    # print(t_vec) """
    # vec is a <class 'Vector'>
    # create a rotation matrix
    # t_mat_rot = Matrix.Rotation(math.radians(83.0), 3, 'X')
    # print("t_mat_rot =")
    # print(t_mat_rot)
    # mat_rot is a <class 'Matrix'>
    # combine transformations
    # t_mat_out = t_mat_rot @ t_vec
    # print("t_mat_out =")
    # print(t_mat_out)
    
    t_espessura_parede = 0.15
    t_inclinação_parede_graus = 90.00
    t_inclinação_parede_radianos = math.radians(t_inclinação_parede_graus)
    print("t_inclinação_parede_radianos =")
    print(t_inclinação_parede_radianos)
    if t_value_x < 0:
        t_espessura_parede *= -1
    t_data = bpy.data.meshes.new(name="meshData")
    # data is a <class 'bpy_types.Mesh'>
    print("1 t_data =")
    print(t_data.values())
    t_data.from_pydata(
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
                    bpy.context.scene.cursor.location[0] + t_value_x * math.sin(t_inclinação_parede_radianos),
                    bpy.context.scene.cursor.location[1] + t_value_x * math.cos(t_inclinação_parede_radianos),
                    bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    bpy.context.scene.cursor.location[0] + t_value_x * math.sin(t_inclinação_parede_radianos) - t_espessura_parede * math.sin(t_inclinação_parede_radianos),
                    bpy.context.scene.cursor.location[1] + t_value_x * math.cos(t_inclinação_parede_radianos) + t_espessura_parede * math.cos(t_inclinação_parede_radianos),
                    bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    bpy.context.scene.cursor.location[0] - t_espessura_parede * math.sin(t_inclinação_parede_radianos),
                    bpy.context.scene.cursor.location[1] + t_espessura_parede * math.cos(t_inclinação_parede_radianos),
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
    t_object = bpy.data.objects.new(
        name="meshObject",
        object_data=t_data
    )

    verts = len(t_data.vertices)
    print("verts INCLINADO = ")
    print(verts)
    print("verts0 = ")
    print(t_data.vertices[0].co)
    print("verts1 = ")
    print(t_data.vertices[1].co)
    print("verts2 = ")
    print(t_data.vertices[2].co)
    print("verts3 = ")
    print(t_data.vertices[3].co)

    # object is a <class 'bpy_types.Object'>
    AddMaterial.add(t_object, "MaterialParedeBranca")
    bpy.context.scene.collection.objects.link(t_object)
  
    # horiRot = rotMat(theta, 3, 'X')
    #                             vertRot = rotMat(phi, 3, 'Z')
    #                             basisVecX.rotate(horiRot)


# Class
class AddMesh():
    """Create a new Mesh Object from data: vertices, edges and faces"""

    # Class execution
    def add(t_structure):
        processar_estrutura(t_structure)
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
