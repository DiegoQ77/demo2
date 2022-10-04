import os


def search_files(path, extension):
    files_array = []
    with os.scandir(path) as path_entry:
        for f in path_entry:
            if f.name.endswith(extension):
                files_array.append(f.path)
        return files_array


def read_data(files):

    list_data_files = []
    for file in files:
        if os.path.exists(file):
            with open(file, 'r') as file_name:
                data = file_name.read()
                if data is not None:
                    list_data_files.append(data)
    return list_data_files
