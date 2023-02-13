import os

def get_path(path : str) -> str:
    path = os.path.normpath(path)
    
    return path