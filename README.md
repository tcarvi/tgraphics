# tgraphics  

- Default output folders: 
    - rendering output: render_output/
    - saving blender file: blender_projects/

#### Windows Command Line Options:
###### Se utilizados, os parâmetros -s e -r devem seguir a ordem definida.
- ```blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_objects_from_input_data.py```  
- ```blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_objects_from_input_data.py -- -s="blenderFileName.blend" -r="renderFileName" ```
- ```blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_objects_from_input_data.py -- -s="blenderFileName.blend" ```
- ```blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_objects_from_input_data.py -- -r="renderFileName" ```

#### Linux ( a atualizar ... )
```blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data.py -- nopyargs```

###### Notice:
- ```--factory-startup``` is used to avoid the user default settings from interfering with automated scene generation.
- ```--``` causes blender to ignore all following arguments so python can use them.
- See blender --help for details.


