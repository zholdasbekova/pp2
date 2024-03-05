import os

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        return True
    else:
        return False

file_to_delete = "/path/to/your/file_to_delete.txt"
if delete_file(file_to_delete):
    print("File deleted successfully.")
else:
    print("File does not exist or could not be deleted.")