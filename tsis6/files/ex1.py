import os

def list_directories_and_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    
    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

path = "\Users\Aidana Zholdasbekova\Desktop\pp\tsis1\ex1"
list_directories_and_files(path)
