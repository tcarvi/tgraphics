bl_info = {
    "name": "Export to SVG image",
    "version": (1, 0, 0, 0),
    "location": "View3D > Properties",
    "description": "Generate an SVG file",
    "category": "Import-Export"}

import bpy, os

class ExportSVG(bpy.types.Operator):
    bl_idname = 'export.svg'
    bl_label = 'Export SVG'
    bl_description = 'Generate an SVG file'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        sce = bpy.context.scene
        wm = bpy.context.window_manager

        # To generate SVG from all frames
        frame_list = range(sce.frame_start, sce.frame_end)
        restore_frame = sce.frame_current

        def drawFloor():
            print("to do drawFloor()")

        for frameCounter in frame_list:
            sce.frame_set(frameCounter)
            # Atom adds frame number to file name.
            userPathWithName = os.path.splitext(wm.ruta)[0]
            fileFormat = os.path.splitext(wm.ruta)[1]
            sceneName = sce.name
            frameNumber = str(int(sce.frame_current)).zfill(4)
            new_ruta = bpy.path.abspath('%s_%s_%s_%s' % (userPathWithName, sceneName, frameNumber, fileFormat))

            # abrir archivo para escribir
            dibujo = open(new_ruta, 'w').write
            if wm.use_continuar:
                for nl in datos[:-3]: dibujo(nl)
                dibujo('\n\n<!-- new blender session -->\n\n\n')
            else:
                x = str(sce.render.resolution_x)
                y = str(sce.render.resolution_y)
                dibujo('<svg width="'+x+'px" height="'+y+'px" viewBox="0 0 '+x+' '+y+'" xmlns="http://www.w3.org/2000/svg" version="1.2" zoomAndPan="disable" preserveAspectRatio="none" focusable="false">\n\n')
                drawFloor()
                dibujo('\n\n</svg>')
        sce.frame_set(restore_frame)
        return{'FINISHED'}


class IncrSVG(bpy.types.Operator):
    bl_idname = 'add_to.svg'
    bl_label = 'Add to SVG'
    bl_description = 'Add shapes to the end of a file'

    def execute(self, context):
        wm = bpy.context.window_manager
        wm.use_continuar = True
        bpy.ops.export.svg()
        if wm.use_continuar == False:
            self.report({'ERROR'}, 'Can not append to this file')
        wm.use_continuar = False
        bpy.ops.ed.undo()
        return{'FINISHED'}


class ComprSVG(bpy.types.Operator):
    bl_idname = 'compress.svg'
    bl_label = 'Compress'
    bl_description = 'Compress selected file to an SVGZ file'

    def execute(self, context):
        import gzip
        wm = bpy.context.window_manager
        if wm.ruta.endswith('.svg'):
            svzruta = wm.ruta+'z'
            try:
                with open(wm.ruta, 'rb') as entrada:
                    with gzip.open(svzruta, 'wb') as salida:
                        salida.writelines(entrada)
            except:
                self.report({'ERROR'}, 'Verify the path')
        else: self.report({'ERROR'}, 'Verify the path')

        return{'FINISHED'}


class OpenSVG(bpy.types.Operator):
    bl_idname = 'open.svg'
    bl_label = 'Open'
    bl_description = 'Open the file'

    def execute(self, context):
        wm = bpy.context.window_manager
        try: bpy.ops.wm.url_open(url=wm.ruta)
        # try: bpy.ops.wm.path_open(filepath=wm.ruta)
        except: pass
        return{'FINISHED'}


class PanelSVG(bpy.types.Panel):
    bl_label = 'Export SVG Image'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        wm = bpy.context.window_manager
        layout = self.layout
        column = layout.column()
        split = column.split(align=True)
        split.operator('export.svg', text='Export SVG')
        split.operator('add_to.svg')
        column.prop(wm, 'ruta')
        split = column.split()
        split.operator('open.svg')
        split.operator('compress.svg')

bpy.types.WindowManager.ruta=bpy.props.StringProperty(name='', subtype='FILE_PATH',
        default='C:\\libs\\projectsBlender\\Scripts\\output\\test.svg', description='Save the SVG file - use absolute path')
bpy.types.WindowManager.use_continuar=bpy.props.BoolProperty(name='Add to SVG',
        default=False, description='Adds geometry to the end of a file')

def register():
    bpy.utils.register_class(ExportSVG)
    bpy.utils.register_class(OpenSVG)
    bpy.utils.register_class(IncrSVG)
    bpy.utils.register_class(ComprSVG)
    bpy.utils.register_class(PanelSVG)


def unregister():
    bpy.utils.unregister_class(ExportSVG)
    bpy.utils.unregister_class(OpenSVG)
    bpy.utils.unregister_class(IncrSVG)
    bpy.utils.unregister_class(ComprSVG)
    bpy.utils.unregister_class(PanelSVG)
 
if __name__ == "__main__":
    register()