import os


def read_files(self, paths):
    if paths != 'str':
        return 'Arquivo não encontrado'
    with open(paths) as paths_files:
        files = os.read(paths_files)
        print(type(files))
        # for files in paths_files:
        #    print(type(files))
        #    return files


read_files('C:\Developer\dataAnalytics\dados\arquivo_teste_02.wnd')
