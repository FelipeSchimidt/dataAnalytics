import os


def read_files(paths):
    # if paths != 'str':
    #    print('Arquivo não encontrado')
    with open(paths) as paths_files:
        for lines in paths_files:
            print(lines)
            return lines
        # for files in paths_files:
        #    print(type(files))
        #    return files


read_files('C://Developer//dataAnalytics//dados//arquivo_teste_02.wnd')
