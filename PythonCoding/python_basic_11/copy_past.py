
import os

class CopyAndPast(object):



    def __init__(self,spath,tpath):
        self._spath = spath
        self._tpath = tpath
        self._pathData = None


    def openPath(self):
        f = open(self._spath,'rb')
        self._pathData = f.read()
        print('当前二进制数%s'%{self._pathData})
        if f:
            f.close()

    def copyPath(self):
        f = open(self._tpath,'wb')
        f.write(self._pathData)
        if f:
            f.close()


class CopyPath(object):

    def __init__(self,path):
        self._path = path
        self._files = None

    def runCopy(self):
        for root,dirs,files in os.walk(self._path):
            print('Root:%s'%root)
            print('Dirs:%s'%dirs)
            print('Files:%s'%files)
            self._files = files

    def copyWithFile(self):
        for file in self._files:
            with open('%s/%s'%(self._path,file),'rb') as f_copy:
                data = f_copy.read()
            with open('/Users/zhaocaifeng/Desktop/SP/%s'%(file),'wb') as f_past:
                f_past.write(data)





if __name__ == '__main__':
    # c = CopyAndPast('source.png','source_copy.png')
    # c.openPath()
    # c.copyPath()

    c = CopyPath('/Users/zhaocaifeng/Desktop/Auth')
    c.runCopy()
    c.copyWithFile()
