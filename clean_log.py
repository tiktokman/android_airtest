import os  
  
# 枚举dirPath目录下的所有文件  
  
fileDir = os.path.dirname(os.path.realpath(__file__)) +'\log'    
for root, dirs, files in os.walk(fileDir):  
#begin  
    print(root)  
    print(dirs)  
    print(files)
    for name in files:
    	os.remove(os.path.join(root, name))  

