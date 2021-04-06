from os import listdir
import os
from os.path import isfile, join
extension=".jpg"
folder="Stairs"
print(listdir(folder))
num=0
for file in listdir(folder):
  print(num)
  os.rename(join(folder, file),join(folder,str(num)+extension))
  num+=1
print(listdir(folder))

