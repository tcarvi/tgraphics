# <pep8-80 compliant>
import bpy


# Class
class AddMetaball:
    """ADD metaball with input location"""

    # Class execution
    @classmethod
    def add(cls) -> str:
        _add_object()
        return {'FINISHED'}


# non-public method
def _add_object() -> None:
    # TODO - To define input
    t_location_input = 2.0, 2.0, 5.0
    # TODO - To add


# To register
def register():
    bpy.utils.register_class(AddMetaball)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddMetaball)


# Register
# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "main", 
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
