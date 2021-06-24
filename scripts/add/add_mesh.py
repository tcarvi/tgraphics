# <pep8-80 compliant>
import bpy
from mathutils import Vector, Matrix
from move_entry_point import MoveEntryPoint
import json
import math
from add_material import AddMaterial
import numpy as np

def add_object(t_structure):
    # processar_estrutura
    # MoveEntryPoint.centralizar()
    print("\n\n\n\n\n\n\n")
    print("################################")
    print(t_structure)
    # [[30, 8.8, 3.0], [10, 3.0, 3.0], [30, 8.3, 3.0], [21, 22.9], [20, -20.0], [1, -3.0], [21, -21.85]]
    # Códigos [0-9]:
    #     0 Deslocamento ortogonal em X
    #     1 Deslocamento ortogonal em Y
    #     2 Deslocamento ortogonal em Z
    # Códigos [10-19]:
    #     10 Deslocamento inclinado em X
    #     11 Deslocamento inclinado em Y
    #     12 Deslocamento inclinado em Z
    # Códigos [20-29]:
    #     20 Retângulo ortogonal de 0.15 em X
    #     21 Retângulo ortogonal de 0.15 em Y
    # Códigos [30-39]:
    #     30 Retângulo inclinado de 0.15 em X
    #        d[1] -> t_comprimento_parede
    #        d[2] -> t_inclinação_parede_graus_EixoX
    #     31 Retângulo inclinado de 0.15 em Y
    # Comandos: 30 -> Retângulo inclinado de 0.15 em X
    #                   No valor de 8.8
    #           10 -> Deslocamento inclinado em X
    #           30 -> Retângulo inclinado de 0.15 em X
    #           21 -> Retângulo ortogonal de 0.15 em Y
    #           20 -> Retângulo ortogonal de 0.15 em X
    #           1  -> Deslocamento ortogonal em Y
    #           21 -> Retângulo ortogonal de 0.15 em Y
    for d in t_structure:
        # Each item "d" is a <class 'list'>
        # print("#LOG: FROM LOOP -> bpy.context.scene.cursor.location[0] =" , bpy.context.scene.cursor.location[0])
        print("\n\n")
        print("Antes: bpy.context.scene.cursor.location[0] = ", bpy.context.scene.cursor.location[0])
        print("Antes: bpy.context.scene.cursor.location[1] = ", bpy.context.scene.cursor.location[1])
        print("Antes: bpy.context.scene.cursor.location[2] = ", bpy.context.scene.cursor.location[2])
        print("\n")
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
                # Desloca posição de inserção
                print("\n\n#LOG: Now, d[0] = ", d[0])
                t_medida_deslocamentoX = d[1]
                t_inclinação_deslocamento_graus = d[2]
                t_inclinação_deslocamento_radianos = math.radians(t_inclinação_deslocamento_graus)
                bpy.context.scene.cursor.location[0] = bpy.context.scene.cursor.location[0] + t_medida_deslocamentoX * math.cos(t_inclinação_deslocamento_radianos)
                bpy.context.scene.cursor.location[1] = bpy.context.scene.cursor.location[1] + t_medida_deslocamentoX * math.sin(t_inclinação_deslocamento_radianos)                
                bpy.context.view_layer.update()
                print("changed bpy.context.scene.cursor.location[0] = ", bpy.context.scene.cursor.location[0])
                print("changed bpy.context.scene.cursor.location[1] = ", bpy.context.scene.cursor.location[1])
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
                # print("add_parede_15_centimetros_horizontal")
                add_parede_15_centimetros_horizontal(d[1])
                bpy.context.scene.cursor.location[0] += d[1]
                bpy.context.view_layer.update()
                continue
            if d[0] == 21:
                print("\n\n#LOG: Now, d[0] = ", d[0])
                # Desenha parede de 0.15 metros de largura, no eixo Y
                # print("add_parede_15_centimetros_transversal")
                add_parede_15_centimetros_transversal(d[1])
                bpy.context.scene.cursor.location[1] += d[1]
                bpy.context.view_layer.update()
                print("changed bpy.context.scene.cursor.location[0] = ", bpy.context.scene.cursor.location[0])
                print("changed bpy.context.scene.cursor.location[1] = ", bpy.context.scene.cursor.location[1])
                continue
            continue
        if d[0] < 40:
            if d[0] == 30:
                print("\n\n#LOG: Now, d[0] = ", d[0])
                # Desenha parede de 0.15 metros de largura, no eixo X inclinado
                # print("#LOG: AddingParede15CentimetrosInclinadaEmX")
                # print("#LOG: bpy.context.scene.cursor.location[0] =" , bpy.context.scene.cursor.location[0])
                t_comprimento_parede = d[1]
                # print("#LOG: Medida da parede = ", t_comprimento_parede)
                t_inclinação_parede_graus = d[2]
                # print("#LOG: Medida da inclinação da parede em graus = ", t_inclinação_parede_graus)
                t_inclinação_parede_radianos = math.radians(t_inclinação_parede_graus)
                # print("#LOG: Medida da inclinacao da parede em radianos = ", t_inclinação_parede_radianos)
                add_parede_15_centimetros_inclinado_em_x(t_comprimento_parede, t_inclinação_parede_radianos)
                bpy.context.scene.cursor.location[0] += t_comprimento_parede * math.cos(t_inclinação_parede_radianos)
                bpy.context.scene.cursor.location[1] += t_comprimento_parede * math.sin(t_inclinação_parede_radianos)
                bpy.context.view_layer.update()
                print("changed bpy.context.scene.cursor.location[0] = ", bpy.context.scene.cursor.location[0])
                print("changed bpy.context.scene.cursor.location[1] = ", bpy.context.scene.cursor.location[1])
                # print("#LOG: added parede_15_centimetros_inclinado_em_x")
                continue
            if d[0] == 31:
                # Desenha parede de 0.15 metros de largura, no eixo Y inclinado
                # print("add_parede_15_centimetros_inclinado_em_y")
                add_parede_15_centimetros_inclinado_em_x(d[1])
                bpy.context.scene.cursor.location[1] += d[1]
                bpy.context.view_layer.update()
                continue
            continue
    # print(bpy.context.scene.cursor.rotation_euler)

def add_parede_15_centimetros_horizontal(t_value_x):
    t_value_y = 0.15
    t_value_inclinacao = 0.00
    add_parede(t_value_x, t_value_y, t_value_inclinacao)

def add_parede_15_centimetros_transversal(t_value_y):
    t_value_x = 0.15
    t_value_inclinacao = 0.00
    add_parede(t_value_x, t_value_y, t_value_inclinacao)

def add_parede_15_centimetros_inclinado_em_x(t_value_x, t_value_inclinacao):
    t_value_y = 0.15
    add_parede(t_value_x, t_value_y, t_value_inclinacao)
    
def add_parede(t_value_x, t_value_y, t_value_inclinacao):
    if t_value_x < 0:
        t_value_y *= -1
    t_data = bpy.data.meshes.new(name="meshData")
    # data is a <class 'bpy_types.Mesh'>
    # print("t_data = ", t_data)
    # print("t_data.values() = ", t_data.values())
    # print("bpy.context.scene.cursor.location[0] = ", bpy.context.scene.cursor.location[0])
    # print("bpy.context.scene.cursor.location[1] = ", bpy.context.scene.cursor.location[1])
    # print("bpy.context.scene.cursor.location[2] = ", bpy.context.scene.cursor.location[2])
    print("t_value_inclinacao = ", t_value_inclinacao)
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
                    bpy.context.scene.cursor.location[0] + t_value_x * math.cos(t_value_inclinacao),
                    bpy.context.scene.cursor.location[1] + t_value_x * math.sin(t_value_inclinacao),
                    bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    bpy.context.scene.cursor.location[0] + t_value_x * math.cos(t_value_inclinacao) - t_value_y * math.sin(t_value_inclinacao),
                    bpy.context.scene.cursor.location[1] + t_value_x * math.sin(t_value_inclinacao) + t_value_y * math.cos(t_value_inclinacao),
                    bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    bpy.context.scene.cursor.location[0] - t_value_y * math.sin(t_value_inclinacao),
                    bpy.context.scene.cursor.location[1] + t_value_y * math.cos(t_value_inclinacao),
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
    # print("bpy.context.scene.cursor.location[0] = ", bpy.context.scene.cursor.location[0])
    # print("t_object = ", t_object)
    verts = len(t_data.vertices)
    # print("verts INCLINADO = ", verts)
    print("verts0 = ", t_data.vertices[0].co)
    print("verts1 = ", t_data.vertices[1].co)
    print("verts2 = ", t_data.vertices[2].co)
    print("verts3 = ", t_data.vertices[3].co)

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
        # print("#LOG: Adding Mesh: ...")
        add_object(t_structure)
        # print("#LOG: Mesh added")
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
