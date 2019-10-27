import sys

DiretorioScriptsAdd = 'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\add'
if DiretorioScriptsAdd not in sys.path:
    sys.path.append(DiretorioScriptsAdd)

DiretorioScriptsIO = 'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\io'
if DiretorioScriptsIO not in sys.path:
    sys.path.append(DiretorioScriptsIO)

DiretorioInputData = 'C:\\libs\\python\\src\\github.com\\tgraphics\\input_data'
if DiretorioInputData not in sys.path:
    sys.path.append(DiretorioInputData)