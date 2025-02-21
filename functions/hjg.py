import os

liste = os.listdir(path)
os.path.join(x,y)
os.path.exists(path)
os.makedirs
os.isdir(path)

def f(start_path):
    file_or_folders = os.listdir(start_path)
    for ff in file_or_folders:
    new_path = os.path.join(start_path, ff)
        if os.path.isdir(new_path):
            f(new_path)
        else:
            #dosya
            print(new__path)


print(f(start_path="."))

def f(start_path, search_pattern):
    file_or_folders = os.listdir(start_path)
    for ff in file_or_folders:
    new_path = os.path.join(start_path, ff)
        if os.path.isdir(new_path):
            f(start_path=new_path, search_pattern=search_pattern)
        else:
            if search_pattern in ff:
                print(new__path)

print(f(start_path="." , search_pattern=".md"))


#json incele