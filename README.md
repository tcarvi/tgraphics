# tgraphics  
#### Command line executions:

- Output folders: 
    - rendering output: tgraphics/render_output/
    - saving blender file: tgraphics/blender_projects/

#### Linux
```blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/adding-objects_job.py -- nopyargs```

#### Windows
```blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\adding-objects_job.py -- nopyargs```

###### Notice:
- ```--factory-startup``` is used to avoid the user default settings from interfering with automated scene generation.
- ```--``` causes blender to ignore all following arguments so python can use them.
- See blender --help for details.