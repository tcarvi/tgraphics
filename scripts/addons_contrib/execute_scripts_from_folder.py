#----------------------------------------------------------
# Add-on
# Execute scripts from Python files of Projects
#----------------------------------------------------------

bl_info = {
    'name': 'Automate execution of scripts from files',
    'author': 'Eduardo dos Santos Leal',
    'version': (1, 0, 0),
    'blender': (2, 78, 0),
    'location': 'View3D > TOOL_PROPS > Scripts from Folder',
    'description': 'Automate execution of scripts from folder',
    'warning': '',
    'wiki_url': '',
    'tracker_url': '',
    'support': 'COMMUNITY',
    'category': 'Scripting'}

import bpy
 
#
#    Menu in toolprops region
#
class ToolPropsPanel(bpy.types.Panel):
    bl_label = "Scripts from Folder"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOL_PROPS"
 
    def draw(self, context):
        layout = self.layout

        layout.label("Verificações e Configurações:", icon='ACTION')
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("scriptfile.button", text="Verificações", icon='TEXT').loc="verification"
        row.operator("scriptfile.button", text="Configuração Inicial", icon='TEXT').loc="configuration"

        layout.label("Ambiente:")
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("scriptfile.button", text="Câmeras", icon='TEXT').loc="cameras"
        row.operator("scriptfile.button", text="Lâmpadas", icon='LAMP_DATA').loc="lamps"

        layout.label("Paredes (até 99)", icon='ACTION')
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("scriptfile.button", text="Script 1", icon='TEXT').loc="1"
        row.operator("scriptfile.button", text="Script 2", icon='TEXT').loc="2"
        row.operator("scriptfile.button", text="Script 3", icon='TEXT').loc="3"
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("scriptfile.button", text="Script 4", icon='TEXT').loc="4"
        row.operator("scriptfile.button", text="Script 5", icon='TEXT').loc="5"
        row.operator("scriptfile.button", text="Script 6", icon='TEXT').loc="6"
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("scriptfile.button", text="Script 7", icon='TEXT').loc="7"
        row.operator("scriptfile.button", text="Script 8", icon='TEXT').loc="8"
        row.operator("scriptfile.button", text="Script 9", icon='TEXT').loc="9"

#
#   Button for execution
#
class OBJECT_OT_Button(bpy.types.Operator):
    bl_idname = "scriptfile.button"
    bl_label = "Execute Scriptfiles"
    loc = bpy.props.StringProperty()
 
    def execute(self, context):
        if self.loc:
            words = self.loc
            filename = "C:\libs\ProjectsBlender\Scripts\{!s}.py".format(self.loc)
            exec(compile(open(filename).read(), filename, 'exec'))
        return{'FINISHED'}

#
#	Registration
#

def register():
    bpy.utils.register_module(__name__)
 
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()