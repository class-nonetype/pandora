import shutil
import os

def clear_project(get_path, **struct):
    for key in struct.keys():
        for value in struct[key].values():
            for scanner in os.scandir(get_path(value)):
                if '__pycache__' in scanner.name:
                    shutil.rmtree(get_path(scanner.path))
