import bpy
import sys
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


def save_blenderfile(blenderfilename):
    save_path = os.path.join(
        os.path.abspath("."),
        "blender_projects\\" + blenderfilename
    )
    SAVE_blenderfile.execute(userfilepath=save_path)


def save_rendering(filename):
    render_path = os.path.join(
        os.path.abspath("."),
        "render_output\\" + filename
    )
    SAVE_rendering.execute(userfilepath=render_path)


def executions():
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

    executions()

    default_save_path = "f1.blend"
    save_blenderfile(default_save_path)
    default_render_path = "r1"
    save_rendering(default_render_path)


def run_with_args(save_path, render_path):

    executions()

    if save_path is None:
        default_save_path = "f1.blend"
        save_blenderfile(default_save_path)
    else:
        save_blenderfile(save_path)

    if render_path is None:
        default_render_path = "r1"
        save_rendering(default_render_path)
    else:
        save_rendering(render_path)


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
        "--python ADD_PATHS_SCRIPT --python GRAPHICS_SCRIPT  [-- options]"
    )
    parameter_s = "-s"
    parameter_r = "-r"
    dest_s = "save_path"
    dest_r = "render_path"
    metavar_s = '="BLENDER_FILE"',
    metavar_r = '="RENDER_FILE"',
    help_s = 'Default: ="blender_projects/f10.blender"'
    help_r = 'Default: ="render_output/r10.png"'
    help_your_input = 'Using your command line argument ...'

    parser = argparse.ArgumentParser(description=usage_text)

    if len(argv) == 1 and argv[0][1] == "s":
        print("option s")
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
            save_path=args.save_path,
            render_path=None
        )
    elif len(argv) == 1 and argv[0][1] == "r":
        print("option r")
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
            save_path=None,
            render_path=args.render_path
        )
    elif len(argv) == 2 and argv[0][1] == "s" and argv[1][1] == "r":
        print("option s and r")
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
            save_path=args.save_path,
            render_path=args.render_path
        )
    elif len(argv) == 0:
        print("no option")
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
