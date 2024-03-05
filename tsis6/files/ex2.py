import os

def check_access(path):
    print("Existence:", os.path.exists(path))
    print("Readability:", os.access(path, os.R_OK))
    print("Writability:", os.access(path, os.W_OK))
    print("Executability:", os.access(path, os.X_OK))

path = "/Users/Aidana Zholdasbekova/Desktop/pp/tsis6/files/ex1.py"
check_access(path)