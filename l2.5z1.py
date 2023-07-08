import os

def split_path(file_path):
    file_dir, file_name = os.path.split(file_path)
    file_name, file_ext = os.path.splitext(file_name)
    return file_dir, file_name, file_ext

path = "/home/user/documents/example.txt"
result = split_path(path)
print(result)
