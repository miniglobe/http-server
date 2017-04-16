import os

def check_exists(documentroot,path):

    if os.path.isfile(documentroot + path):
        return True
    else:
        return False
