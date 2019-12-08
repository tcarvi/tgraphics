# <pep8-80 compliant>
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
from add_light import AddLight
# from add_light_probe import AddLightProbe
from add_camera import AddCamera
# from add_speaker import AddSpeaker
# from add_force_field import AddForceField
from save_blender_file import SaveBlenderFile
from save_rendering import SaveRendering
from input_planta_structure import t_structure
from input_lighting_positions import t_lighting
from list_objects import ListObjects
from list_scenes import ListScenes
from list_materials import ListMaterials
from evaluate_time import EvaluateTime


def generate_objects_from_structure():
    # Clear existing objects.
    bpy.ops.wm.read_factory_settings(use_empty=True)
    # Adding new objects
    AddMesh.add(t_structure)  # Mesh
    print("Começo")
    AddLight.add(t_lighting[0])  # Camera
    print("Fim")
    AddCamera.add()  # Camera
    bpy.context.view_layer.update()


def run_no_args():
    generate_objects_from_structure()
    t_default_save_file_name = "f1.blend"
    SaveBlenderFile.save(t_blender_file_name=t_default_save_file_name)
    t_default_render_output_name = "r1"
    SaveRendering.save(t_rendering_file_name=t_default_render_output_name)


def run_with_args(t_save_file_name, t_render_output_name):
    generate_objects_from_structure()
    if t_save_file_name is None:
        t_default_save_file_name = "f1.blend"
        SaveBlenderFile.save(t_blender_file_name=t_default_save_file_name)
    else:
        SaveBlenderFile.save(t_blender_file_name=t_save_file_name)
    if t_render_output_name is None:
        t_default_render_output_name = "r1"
        SaveRendering.save(t_rendering_file_name=t_default_render_output_name)
    else:
        SaveRendering.save(t_rendering_file_name=t_render_output_name)


def main():
    import sys
    import argparse

    t_argv = sys.argv
    if "--" in t_argv:
        t_index = t_argv.index("--")
        for i in range(t_index, -1, -1):
            del t_argv[i]
    else:
        t_argv = []
    t_usage_text = (
        "Customized usage: $ blender --background --factory-startup"
        " --python ADD_PATHS_SCRIPT --python ADD_GRAPHICS_SCRIPT  [-- options]"
    )
    t_parameter_s = "-s"
    t_parameter_r = "-r"
    t_dest_s = "save_file_name"
    t_dest_r = "render_output_name"
    t_metavar_s = '-s="BLENDER_FILE"',
    t_metavar_r = '-r="RENDER_FILE"',
    t_help_s = 'Default: -s="f1.blender"'
    t_help_r = 'Default: -r="r1.png"'
    t_help_your_input = "Using your command line argument ..."
    t_parser = argparse.ArgumentParser(description=t_usage_text)
    if len(t_argv) == 1 and t_argv[0][1] == "s":
        t_parser.add_argument(
            t_parameter_s,
            dest=t_dest_s,
            metavar=t_metavar_s,
            help=t_help_your_input
        )
        t_parser.add_argument(
            t_parameter_r,
            dest=t_dest_r,
            metavar=t_metavar_r,
            help=t_help_r
        )
        t_parser.print_help()
        t_args = parser.parse_args(t_argv)
        t_time_of_execution = 0.00
        EvaluateTime.init(t_time_of_execution)
        run_with_args(
            t_save_file_name=t_args.save_file_name,
            t_render_output_name=None
        )
        EvaluateTime.evaluate_time(t_time_of_execution)
    elif len(t_argv) == 1 and t_argv[0][1] == "r":
        parser.add_argument(
            t_parameter_s,
            dest=t_dest_s,
            metavar=t_metavar_s,
            help=t_help_s
        )
        parser.add_argument(
            t_parameter_r,
            dest=t_dest_r,
            metavar=t_metavar_r,
            help=t_help_your_input
        )
        t_parser.print_help()
        t_args = parser.parse_args(t_argv)
        t_time_of_execution = 0.00
        EvaluateTime.init(t_time_of_execution)
        run_with_args(
            t_save_file_name=None,
            t_render_output_name=t_args.render_output_name
        )
        EvaluateTime.evaluate_time(t_time_of_execution)
    elif len(t_argv) == 2 and t_argv[0][1] == "s" and t_argv[1][1] == "r":
        parser.add_argument(
            t_parameter_s,
            dest=t_dest_s,
            metavar=t_metavar_s,
            help=t_help_your_input
        )
        parser.add_argument(
            t_parameter_r,
            dest=t_dest_r,
            metavar=t_metavar_r,
            help=t_help_your_input
        )
        t_parser.print_help()
        t_time_of_execution = 0.00
        EvaluateTime.init(t_time_of_execution)
        t_args = t_parser.parse_args(t_argv)
        run_with_args(
            t_save_file_name=args.t_save_file_name,
            t_render_output_name=t_args.render_output_name
        )
        EvaluateTime.evaluate_time(t_time_of_execution)
    elif len(t_argv) == 0:
        t_parser.add_argument(
            t_parameter_s,
            dest=t_dest_s,
            metavar=t_metavar_s,
            help=t_help_s
        )
        t_parser.add_argument(
            t_parameter_r,
            dest=t_dest_r,
            metavar=t_metavar_r,
            help=t_help_r
        )
        t_parser.print_help()
        t_time_of_execution = 0.00
        EvaluateTime.init(t_time_of_execution)
        run_no_args()
        EvaluateTime.evaluate_time(t_time_of_execution)
    print("\nList of data objects:")
    ListObjects.list()
    print("\nList of data scenes:")
    ListScenes.list()
    print("\nList of data materials:")
    ListMaterials.list()
    print("\nBatch job finished, exiting ...")


if __name__ == "__main__":
    main()
