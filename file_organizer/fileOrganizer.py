import os
import shutil

path = input("Enter path") # creating a variable called path which takes the input of the directory path that you want to organize
files = os.listdir(path) #creating variable called files which consists of list of files


for file in files:# ussing loops we traverse every file from files
    filename,extension = os.path.splitext(file) # we split the filename and extension of the file
    extension = extension[1:] # removing the dot from the extension through slicing.

    if os.path.exists(path+'/'+extension): #if the extension directory already exists, then we move the file to that directory.
        shutil.move(path+'/'+file, path+'/'+ extension+'/'+file)
    
    else:
        os.makedirs(path+'/'+extension) # we make new dir and then we move the file into it
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

# on running the program and entering the path int the terminal all fi=older gets arranged


