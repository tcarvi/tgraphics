import bpy
import os
from add_mesh import AddMesh
# from add_curve import AddCurve
# from add_surface import AddSurface
# from add_metaball import AddMetaball
# from add_text import AddText
# from add_grease_pencil import AddGreasePencil
# from add_armature import AddArmature
# from add_lattice import AddLattice
# from add_empty import AddEmpty
# from add_image import AddImage
# from add_light import AddLight
# from add_light_probe import AddLightProbe
from add_camera import AddCamera
# from add_speaker import AddSpeaker
# from add_force_field import AddForceField
from save_blender_file import SaveBlenderFile
from save_rendering import SaveRendering
from input_planta_structure import structure
from list_objects import ListObjects
from list_scenes import ListScenes


def generate_objects_from_structure():

    # Clear existing objects.
    bpy.ops.wm.read_factory_settings(use_empty=True)

    # Adding new objects
    AddMesh.add(structure)  # Mesh

    AddCamera.add()  # Camera
    bpy.context.view_layer.update()


def run_no_args():

    generate_objects_from_structure()

    default_save_file_name = "f1.blend"
    SaveBlenderFile.execute(blender_file_name=default_save_file_name)
    default_render_output_name = "r1"
    SaveRendering.execute(rendering_file_name=default_render_output_name)


def run_with_args(save_file_name, render_output_name):

    generate_objects_from_structure()

    if save_file_name is None:
        default_save_file_name = "f1.blend"
        SaveBlenderFile.execute(blender_file_name=default_save_file_name)
    else:
        SaveBlenderFile.execute(blender_file_name=save_file_name)

    if render_output_name is None:
        default_render_output_name = "r1"
        SaveRendering.execute(rendering_file_name=default_render_output_name)
    else:
        SaveRendering.execute(rendering_file_name=render_output_name)


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

    print("List of data objects:")
    ListObjects.list()

    print("List of data scenes:")
    ListScenes.list()

    print('\nBatch job finished, exiting ...')


if __name__ == "__main__":
    main()
