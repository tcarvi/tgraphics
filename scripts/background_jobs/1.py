# This script is an example of how you can run blender from the command line
# (in background mode with no interface) to automate tasks, in this example it
# creates a text object, camera and light, then renders and/or saves it.
# This example also shows how you can parse command line options to scripts.
#
# Example usage for this test.
# Linux
# blender --background --factory-startup --python $HOME/background_job.py -- \
#         --text="Hello World" \
#         --render="/tmp/hello" \
#         --save="/tmp/hello.blend"
# Windows
# blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py
# blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\1.py -- --text="Teste" --render="C:\libs\python\src\github.com\tgraphics\render_output\r1" --save="C:\libs\python\src\github.com\tgraphics\blender_projects\f1.blend"
# blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\1.py -- --text="Teste" --render="C:\libs\python\src\github.com\tgraphics\render_output\r1" --save="C:\libs\python\src\github.com\tgraphics\blender_projects\f1.blend"
#
# Notice:
# '--factory-startup' is used to avoid the user default settings from
#                     interfering with automated scene generation.
#
# '--' causes blender to ignore all following arguments so python can use them.
#
# See blender --help for details.

import bpy
import sys
# _thread
# _io
# '__main__': <module '__main__' from 'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\background_jobs\\1.py'>, 
# io
# os
# os.path
# _bpy
# bl_operators
# mathutils
# math
# collections
# operator
# cycles
# enum
# types
# array
# time
# string
from add_mesh import ADD_mesh_from_data
from add_light import ADD_light_with_location
from add_camera import ADD_camera_with_location
from add_text import ADD_text_from_data

def example_function(save_path, render_path):
    
    # Clear existing objects.
    bpy.ops.wm.read_factory_settings(use_empty=True)

    # Text Object
    ADD_text_from_data.execute()

    # Camera
    ADD_camera_with_location.execute()

    # Light
    ADD_light_with_location.execute()  

    # Mesh
    ADD_mesh_from_data.execute()

    bpy.context.view_layer.update()

    print("bpy.data.objects.items() = ")
    print(bpy.data.objects.items())

    if save_path:
        bpy.ops.wm.save_as_mainfile(filepath=save_path)

    if render_path:
        render = bpy.context.scene.render
        render.use_file_extension = True
        render.filepath = render_path
        bpy.ops.render.render(write_still=True)

def main():
    import sys       # to get command line args
    import argparse  # to parse options for us and print a nice help message

    # get the args passed to blender after "--", all of which are ignored by
    # blender so scripts may receive their own arguments
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
