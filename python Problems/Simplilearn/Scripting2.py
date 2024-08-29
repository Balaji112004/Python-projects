from os import path

def createfile(dest):
  if not (path.isfile(dest)):
    f=open(dest,'w')
    f.write("Welcome to python scripting")
    f.write(".Second line is entered")
    f.close()

dest="C:\\Users\\kbala\\OneDrive\\Desktop\\Learning\\Python\\sample.txt"
createfile(dest)
print("File created")