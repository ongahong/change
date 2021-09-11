

class FileUtil:

    def __init__(self):
        print(f'')

    #打开文件
    @staticmethod
    def openFile(filePath,mode):
        print(f'params.filePath:{filePath}; mode:{mode}')
        if(mode == None):
            f = open(filePath)
        else:
            f = open(filePath,mode)
        print(f'result.filePath:{filePath}; mode:{mode}; {f.name}; {f.closed}')
        return f

f = FileUtil.openFile("D:/workspace/pycode/mypython/com/org/u/change/util/FileUtil.py",None)

f.read(20)
f.seek(20,25)
