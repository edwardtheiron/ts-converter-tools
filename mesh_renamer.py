import os, shutil

#to add: delete old files feature
#bugs: file count doesn't work

file_count = 0

def mesh_renamer():    
    # folder path
    dir_path = r"C:\\d\\"
    
    count = False
    # list to store files
    # res = []

    # Iterate target directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            #NEEDS REFACTORING
            if "_1.obj" in path.lower():    
                new_name = "1_0032_"+ path.removesuffix("_1.obj") + ".obj"
                rename(dir_path + path, dir_path + new_name)
            elif "_2.obj" in path.lower():
                new_name = "2_0064_"+ path.removesuffix("_2.obj") + ".obj"
                rename(dir_path + path, dir_path + new_name)
            elif "_3.obj" in path.lower():
                new_name = "3_0256_"+ path.removesuffix("_3.obj") + ".obj"
                rename(dir_path + path, dir_path + new_name)
            elif "_4.obj" in path.lower():
                new_name = "4_1024_"+ path.removesuffix("_4.obj") + ".obj"
                rename(dir_path + path, dir_path + new_name)
    if count == True:
        print(str(file_count) + " files created")

def rename(path, name):
    if not os.path.exists(name):
        shutil.copy(path, name)
        #file_count = file_count + 1

if __name__ == "__main__":
    mesh_renamer()