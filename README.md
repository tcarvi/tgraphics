# tgraphics  

- Requirements: 
    - `install blender` ( https://www.blender.org/ )
    - `install python` ( https://www.python.org/downloads/ )
    - `install git`
- Installation:
    - Criar diretório `C:\libs\python\src\github.com\`
    - `cd C:\libs\python\src\github.com\`
    - `git clone https://github.com/tcarvi/tgraphics.git`
    - `cd tgraphics`
    - `pip install -r requirements.txt`
- Default output folders: 
    - rendering output: `render_output/`
    - saving blender file:  `blender_projects/`

#### Windows - CLI (Command Line Interface):
###### Se utilizados, os parâmetros -s e -r devem seguir a ordem definida.
- ```blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_objects_from_input_data.py```  
- ```blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_objects_from_input_data.py -- -s="blenderFileName.blend" -r="renderFileName" ```
- ```blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_objects_from_input_data.py -- -s="blenderFileName.blend" ```
- ```blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_objects_from_input_data.py -- -r="renderFileName" ```

#### Linux - CLI (Command Line Interface)
```blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data.py```
###### Se utilizados, os parâmetros -s e -r devem seguir a ordem definida.
- ```blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data```  
- ```blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data -- -s="blenderFileName.blend" -r="renderFileName" ```
- ```blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data -- -s="blenderFileName.blend" ```
- ```blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data -- -r="renderFileName" ```

#### MAC OSX - CLI (Command Line Interface)
- ```/Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data.py```
###### Se utilizados, os parâmetros -s e -r devem seguir a ordem definida.

###### Notice:
- ```--factory-startup``` is used to avoid the user default settings from interfering with automated scene generation.
- ```--``` causes blender to ignore all following arguments so python can use them.
- See blender --help for details.


