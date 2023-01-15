import shutil
import os
#print(dir(os))
#print(dir(shutil))

path=os.getcwd()
print(path)
#os.mkdir("suiiiiiiiiii")
c = os.listdir("C:/Users/aleyh/Desktop")
print(c)
d = os.path.exists("C:/Users/aleyh/Desktop/abc")
print(d)
route, ext=os.path.splitext("C:/Users/aleyh/Desktop/mosalah.webp")
print("the route of the file is", route)
print("the ext of the file is", ext)
source = "C:/Users/aleyh/Desktop"
destination = "C:/Users/aleyh/Desktop/abc"
list = os.listdir(source)
for i in list:
    root, ext= os.path.splitext(i)
    print("the route of the file is", root)
    print("the ext of the file is", ext)


#result = shutil.move(source, destination)