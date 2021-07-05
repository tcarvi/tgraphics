# <pep8-80 compliant>
import sys
import bpy
import json
import math
from mathutils import Vector, Matrix
from add_material import AddMaterial
from move_entry_point import MoveEntryPoint
from comando_desenho import EnumComandoDesenho


# Class
class AddMesh:
    """Create a new Mesh Object from data: vertices, edges and faces"""

    # Class execution
    @classmethod
    def add(cls, t_structure):
        # print("#LOG: Adding Mesh: ...")
        _add_object(t_structure)
        # print("#LOG: Mesh added")
        return {'FINISHED'}


# non-public method
def _add_object(t_structure):
    print("\n")
    print("###################### Processando ######################")
    print(t_structure)
    print("\n")
    for d in t_structure:
        print("[Atual] Location do cursor: ", bpy.context.scene.cursor.location)
        if(d[0] < 10):
            if(d[0] == 0):
                # 0 Deslocamento ortogonal em X
                print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
                bpy.context.scene.cursor.location[0] += d[1]
                bpy.context.view_layer.update()
                continue
            if(d[0] == 1):
                # 1 Deslocamento ortogonal em Y
                print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
                bpy.context.scene.cursor.location[1] += d[1]
                bpy.context.view_layer.update()
                continue
            if(d[0] == 2):
                # 2 Deslocamento ortogonal em Z
                print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
                bpy.context.scene.cursor.location[2] += d[1]
                bpy.context.view_layer.update()
                continue
            if(d[0] == 3):
                # Atualiza posição XY
                print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
                bpy.context.scene.cursor.location[0] += d[1]
                bpy.context.scene.cursor.location[1] += d[2]
                bpy.context.view_layer.update()
                continue
            continue
        if(d[0] < 20):
            if(d[0] == 10):
                # 10 Deslocamento inclinado em X
                print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
                t_medida_deslocamentoX = d[1]
                t_inclinação_deslocamento_graus = d[2]
                t_inclinação_deslocamento_radianos = math.radians(t_inclinação_deslocamento_graus)
                bpy.context.scene.cursor.location[0] = bpy.context.scene.cursor.location[0] + t_medida_deslocamentoX * math.cos(t_inclinação_deslocamento_radianos)
                bpy.context.scene.cursor.location[1] = bpy.context.scene.cursor.location[1] + t_medida_deslocamentoX * math.sin(t_inclinação_deslocamento_radianos)
                bpy.context.view_layer.update()
                print("changed bpy.context.scene.cursor.location[0] = ", bpy.context.scene.cursor.location[0])
                print("changed bpy.context.scene.cursor.location[1] = ", bpy.context.scene.cursor.location[1])
                continue
            if(d[0] == 11):
                # 10 Deslocamento inclinado em Y
                print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
                bpy.context.scene.cursor.rotation_euler[1] += math.radians(d[1])
                bpy.context.view_layer.update()
                continue
            if(d[0] == 12):
                # 10 Deslocamento inclinado em Z
                print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
                bpy.context.scene.cursor.rotation_euler[2] += math.radians(d[1])
                bpy.context.view_layer.update()
                continue
            if(d[0] == 13):
                # 10 Deslocamento inclinado em XZ
                print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
                bpy.context.scene.cursor.rotation_euler[0] += math.radians(d[1])
                bpy.context.scene.cursor.rotation_euler[1] += math.radians(d[1])
                bpy.context.view_layer.update()
                continue
            continue
        if(d[0] < 30):
            if(d[0] == 20):
                # Desenhar Retangulo em X
                print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
                t_comprimento_parede = d[1]
                print("Comprimento do deslocamento = ", t_comprimento_parede)
                _add_parede_15_centimetros_em_X(d[1])
                bpy.context.scene.cursor.location[0] += t_comprimento_parede
                # [NÃO MUDA] bpy.context.scene.cursor.location[1] = bpy.context.scene.cursor.location[1]
                bpy.context.view_layer.update()
                print("[Nova] Location do cursor: ", bpy.context.scene.cursor.location)
                print("\n")
                continue
            if(d[0] == 21):
                # Desenhar Retangulo em Y
                print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
                print("Comprimento do deslocamento = ", d[1])
                _add_parede_15_centimetros_em_Y(d[1])
                bpy.context.scene.cursor.location[1] += d[1]
                bpy.context.view_layer.update()
                continue
            continue
        if(d[0] < 40):
            if(d[0] == 30):
                print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
                # 30 Retângulo inclinado de 0.15 em X
                t_comprimento_parede = d[1]
                print("Comprimento da parede = ", t_comprimento_parede)
                t_inclinação_parede_graus = d[2]
                t_inclinação_parede_radianos = math.radians(t_inclinação_parede_graus)
                print("Inclinacao da parede em radianos = ", t_inclinação_parede_radianos)
                _add_parede_15_centimetros_inclinado_em_x(t_comprimento_parede, t_inclinação_parede_radianos)
                bpy.context.scene.cursor.location[0] += t_comprimento_parede * math.cos(t_inclinação_parede_radianos)
                bpy.context.scene.cursor.location[1] += t_comprimento_parede * math.sin(t_inclinação_parede_radianos)
                bpy.context.view_layer.update()
                print("[Nova] Location do cursor: ", bpy.context.scene.cursor.location)
                print("\n")
                continue
            if(d[0] == 31):
                print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
                # 30 Retângulo inclinado de 0.15 em Y
                t_comprimento_parede = d[1]
                t_value_inclinacao = d[2]
                _add_parede_15_centimetros_inclinado_em_x(t_comprimento_parede, t_value_inclinacao)
                bpy.context.scene.cursor.location[1] += t_comprimento_parede
                bpy.context.view_layer.update()
                print("[Nova] Location do cursor: ", bpy.context.scene.cursor.location)
                print("\n")
                continue
            continue


# non-public method
def _add_parede_15_centimetros_em_X(t_value_x: float):
    t_value_y = 0.15
    t_value_inclinacao = 0.00
    _add_parede(t_value_x, t_value_y, t_value_inclinacao)


# non-public method
def _add_parede_15_centimetros_em_Y(t_value_y: float):
    t_value_x = 0.15
    t_value_inclinacao = 0.00
    _add_parede(t_value_x, t_value_y, t_value_inclinacao)


# non-public method
def _add_parede_15_centimetros_inclinado_em_x(t_value_x: float, t_value_inclinacao: float):
    t_value_y = 0.15
    _add_parede(t_value_x, t_value_y, t_value_inclinacao)

# non-public method
def _add_parede_15_centimetros_inclinado_em_Y(t_value_y: float, t_value_inclinacao: float):
    t_value_x = 0.15
    _add_parede(t_value_x, t_value_y, t_value_inclinacao)

# non-public method
def _add_parede(t_value_x: float, t_value_y: float, t_value_inclinacao: float):
    if t_value_x < 0:
        t_value_y *= -1
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
    verts = len(t_data.vertices)
    print("verts0 = ", t_data.vertices[0].co)
    print("verts1 = ", t_data.vertices[1].co)
    print("verts2 = ", t_data.vertices[2].co)
    print("verts3 = ", t_data.vertices[3].co)
    AddMaterial.add(t_object, "MaterialParedeBranca")
    bpy.context.scene.collection.objects.link(t_object)


# To register
def register():
    bpy.utils.register_class(AddMesh)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddMesh)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
# Deve-se conseguir instalar bpy em sys.path para executar teste local!
if __name__ == "__main__":
    # register()
    # Teste
    import sys
    print(sys.path)
    # from ..background_jobs.add_path import AddPath
    # from import bpy
    # AddPath.add()
    # AddMesh.add([[30, 10.0, 60.0], [20, -10.0, 0.0], [31, -10.0, 120.0]])
