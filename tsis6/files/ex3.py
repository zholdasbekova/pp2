import os

def test_existence_and_split_path(path):
    if os.path.exists(path):
        print("Path exists.")
        directory, filename = os.path.split(path)
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("Path does not exist.")

path = "/Users/Aidana Zholdasbekova/Desktop/pp/tsis6/files/ex1.py"
test_existence_and_split_path(path)
