import bpy
import os
from add_mesh import ADD_mesh
# from add_curve import ADD_curve
# from add_surface import ADD_surface
# from add_metaball import ADD_metaball
from add_text import ADD_text
# from add_greasepencil import ADD_greasepencil
from add_armature import ADD_armature
# from add_lattice import ADD_lattice
# from add_empty import ADD_empty
# from add_image import ADD_image
from add_light import ADD_light
# from add_lightprobe import ADD_lightprobe
from add_camera import ADD_camera
# from add_speaker import ADD_speaker
# from add_forcefield import ADD_forcefield
from save_blenderfile import SAVE_blenderfile
from save_rendering import SAVE_rendering


def gerarObjetosConformeEstruturaIndicadaEmArquivo():
    
    # Clear existing objects.
    bpy.ops.wm.read_factory_settings(use_empty=True)

    ADD_mesh.execute()  # Mesh
    # ADD_curve.execute()  # Curve
    # ADD_surface.execute() # Surface
    # ADD_metaball.execute() # Metaball
    ADD_text.execute()  # Text Object
    # ADD_greasepencil.execute()  # Grease Pencil
    ADD_armature.execute()  # Armature
    ADD_light.execute()  # Light
    # ADD_lightprobe.execute()  # LightProbe
    ADD_camera.execute()  # Camera
    # ADD_speaker.execute()  # Speaker
    # ADD_forcefield.execute()  # ForceField
    bpy.context.view_layer.update()


def run_no_args():

    gerarObjetosConformeEstruturaIndicadaEmArquivo()

    default_save_file_name = "f1.blend"
    SAVE_blenderfile.execute(blenderfilename=default_save_file_name)
    default_render_output_name = "r1"
    SAVE_rendering.execute(renderingfilename=default_render_output_name)


def run_with_args(save_file_name, render_output_name):

    gerarObjetosConformeEstruturaIndicadaEmArquivo()

    if save_file_name is None:
        default_save_file_name = "f1.blend"
        SAVE_blenderfile.execute(blenderfilename=default_save_file_name)
    else:
        SAVE_blenderfile.execute(blenderfilename=save_file_name)

    if render_output_name is None:
        default_render_output_name = "r1"
        SAVE_rendering.execute(renderingfilename=default_render_output_name)
    else:
        SAVE_rendering.execute(renderingfilename=render_output_name)


def main():
    import sys
    import argparse

    argv = sys.argv

    if "--" in argv:
        index = argv.index("--")
        counter = 0
        for i in range(index, -1, -1):
            del argv[i]
    else:
        argv = []

    usage_text = (
        "Customized usage: $ blender --background --factory-startup"
        " --python ADD_PATHS_SCRIPT --python ADD_GRAPHICS_SCRIPT  [-- options]"
    )
    parameter_s = "-s"
    parameter_r = "-r"
    dest_s = "save_file_name"
    dest_r = "render_output_name"
    metavar_s = '-s="BLENDER_FILE"',
    metavar_r = '-r="RENDER_FILE"',
    help_s = 'Default: -s="f1.blender"'
    help_r = 'Default: -r="r1.png"'
    help_your_input = 'Using your command line argument ...'

    parser = argparse.ArgumentParser(description=usage_text)

    if len(argv) == 1 and argv[0][1] == "s":
        parser.add_argument(
            parameter_s,
            dest=dest_s,
            metavar=metavar_s,
            help=help_your_input
        )
        parser.add_argument(
            parameter_r,
            dest=dest_r,
            metavar=metavar_r,
            help=help_r
        )
        parser.print_help()
        args = parser.parse_args(argv)
        run_with_args(
            save_file_name=args.save_file_name,
            render_output_name=None
        )
    elif len(argv) == 1 and argv[0][1] == "r":
        parser.add_argument(
            parameter_s,
            dest=dest_s,
            metavar=metavar_s,
            help=help_s
        )
        parser.add_argument(
            parameter_r,
            dest=dest_r,
            metavar=metavar_r,
            help=help_your_input
        )
        parser.print_help()
        args = parser.parse_args(argv)
        run_with_args(
            save_file_name=None,
            render_output_name=args.render_output_name
        )
    elif len(argv) == 2 and argv[0][1] == "s" and argv[1][1] == "r":
        parser.add_argument(
            parameter_s,
            dest=dest_s,
            metavar=metavar_s,
            help=help_your_input
        )
        parser.add_argument(
            parameter_r,
            dest=dest_r,
            metavar=metavar_r,
            help=help_your_input
        )
        parser.print_help()
        args = parser.parse_args(argv)
        run_with_args(
            save_file_name=args.save_file_name,
            render_output_name=args.render_output_name
        )
    elif len(argv) == 0:
        parser.add_argument(
            parameter_s,
            dest=dest_s,
            metavar=metavar_s,
            help=help_s
        )
        parser.add_argument(
            parameter_r,
            dest=dest_r,
            metavar=metavar_r,
            help=help_r
        )
        parser.print_help()
        run_no_args()

    print('\nBatch job finished, exiting ...')


if __name__ == "__main__":
    main()
