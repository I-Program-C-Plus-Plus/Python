import glob
import os

#Author Stephen Nobilio

class File:

    def findFileByType(self,typeOfFile,directory):
        os.chdir(directory)
        files = []
        for file in glob.glob("*.{}".format(typeOfFile)):
            files.append(file)
        return files

    def findFileByName(self,nameOfFile,directory):
        os.chdir(directory)
        files = []
        for file in glob.glob("{}.*".format(nameOfFile)):
            files.append(file)
        return files

    def deleteFileByType(self,typeOfFile,directory):
        os.chdir(directory)
        for file in glob.glob("*.{}".format(typeOfFile)):
            os.remove(file)

    def deleteFileByName(self,nameOfFile,directory):
        os.chdir(directory)
        for file in glob.glob("{}.*".format(nameOfFile)):
            os.remove(file)
            
    def makeFilesByType(self,nameOfFile,typeOfFile,directory,amountOfFiles):
        os.chdir(directory)
        for i in range(0,amountOfFiles):
            file = open("{}({}).{}".format(nameOfFile,i,typeOfFile),"w")            

file = File()
