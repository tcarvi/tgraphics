# Features implemented:
# To run blender from the command line (in background mode with no interface),
# It creates and adds:
# - a mesh object
# - a curve object
# - a surface object
# - a text object
# - a light
# - a camera
# Then it renders a graphics product
# And finally it saves the generated blend file.
#
# Coomand line executions:
#
# Linux
# blender --background --factory-startup --python
#   /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py
#   --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/
#                                                    adding-objects_job.py --
#   --render="/libs/python/src/github.com/tgraphics/render_output/r1"
#   --save="/libs/python/src/github.com/tgraphics/blender_projects/f1.blend"
#
# Windows
# blender --background --factory-startup
#  --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\
#                                                                add_path.py
#  --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\
#                                                   adding-objects_job.py --
#  --render="C:\libs\python\src\github.com\tgraphics\render_output\r1"
#  --save="C:\libs\python\src\github.com\tgraphics\blender_projects\f1.blend"
#
# Notice:
# '--factory-startup' is used to avoid the user default settings from
#                       interfering with automated scene generation.
# '--' causes blender to ignore all following arguments so
#                       python can use them.
# See blender --help for details.

import bpy
import sys
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



def example_function(save_path, render_path):

    # Clear existing objects.
    bpy.ops.wm.read_factory_settings(use_empty=True)

    # Mesh
    ADD_mesh.execute()

    # Curve
    # ADD_curve.execute()

    # Surface
    # ADD_surface.execute()

    # Metaball
    # ADD_metaball.execute()

    # Text Object
    ADD_text.execute()

    # Grease Pencil
    # ADD_greasepencil.execute()

    # Armature
    ADD_armature.execute()

    # Light
    ADD_light.execute()

    # LightProbe
    # ADD_lightprobe.execute()

    # Camera
    ADD_camera.execute()

    # Speaker
    # ADD_speaker.execute()

    # ForceField
    # ADD_forcefield.execute()

    bpy.context.view_layer.update()

    print("bpy.data.objects.items() = ")
    print(bpy.data.objects.items())

    if not save_path:
        save_path = "blender_projects\\f2.blend"
    SAVE_blenderfile.execute(userfilepath=save_path)

    if not render_path:
        render_path = "//..\\render_output\\r2"
    SAVE_rendering.execute(userfilepath=render_path)


def main():
    import sys
    import argparse

    # To get command line args passed to blender after "--", 
    # all of which are ignored by blender so scripts may receive 
    # their own arguments.
    argv = sys.argv

    if "--" not in argv:
        argv = []  # as if no args are passed
    else:
        argv = argv[argv.index("--") + 1:]  # get all args after "--"

    # When --help or no args are given, print this help
    usage_text = (
        "Run blender in background mode with this script:"
        "  blender --background --python " + __file__ + " -- [options]"
    )

    # to parse options and print a nice help message
    parser = argparse.ArgumentParser(description=usage_text)

    parser.add_argument(
        "-s", "--save", dest="save_path", metavar='FILE',
        help="Save the generated file to the specified path",
    )
    parser.add_argument(
        "-r", "--render", dest="render_path", metavar='FILE',
        help="Render an image to the specified path",
    )

    args = parser.parse_args(argv)  # In this example we won't use the args

    if not argv:
        parser.print_help()
        return

    # Run the example function
    example_function(args.save_path, args.render_path)

    print("batch job finished, exiting")


if __name__ == "__main__":
    main()
