from platform import system
import os


def which_os():
    return system()

def which_dirname(filename):
    return os.path.dirname(filename)

def which_path():
    return os.getcwd()


def is_file(path):
    return os.path.isfile(path)


def is_dir(path):
    return os.path.isdir(path)


def ls_dir(path):
    return os.listdir(path)
