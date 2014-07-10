import os

class Utility:

    def __init__(self, filePath):

        #gets path of file running currently
        self.currentPath = filePath

        #a list of sub directories that should exist within root 
        self.subDirs = ('\scramV2', '\game', '\http', '\scram', '\test', '\twisted')

    #check to see if the path contains a subdirectory extension, if so remove it
    def check(self):

        for sub in self.subDirs:

            if sub in self.currentPath:

                cdir = self.currentPath.split(sub, 1)[0]
                
        return cdir

    #find the file within the working directory
    def find(self, name, path):

        for root, dirs, files in os.walk(path):

                  if name in files:

                      return os.path.join(root, name)

    #implement this method to get the file you need find
    def getPath(self, fileName):
                  
        path = self.find(fileName, self.check())

        return path
