from config import osinfo
from config import hashs
from gc import collect
from time import sleep
import argparse


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', dest="type")
    parser.add_argument('--dir', dest="dir")
    parser.add_argument('--file', dest="filename")

    arguments = parser.parse_args()

    typeHash = arguments.type if (arguments.type) else "MD5"
    directory = arguments.dir if (arguments.dir) else (osinfo.which_path())

    if (arguments.filename):
        hashInfo = calculate_hash(arguments.filename, typeHash)
        print_info(hashInfo, arguments.filename)
    else:
        deep_hash(directory, typehash=typeHash)

def deep_hash(directory, typehash=""):
    files = osinfo.ls_dir(directory) if (osinfo.is_dir(directory)) else [directory]
    
    for file in files:
        if (osinfo.is_file(directory + "/" + file)):
            hashFile = calculate_hash(directory + "/" + file, typehash)
            print_info(directory + "/" + file, hashFile)
            collect()

        if (osinfo.is_dir(directory + "/" + file)):
            deep_hash(directory + "/" + file, typehash=typehash)
        sleep(0.5)

def calculate_hash(filename, typehash):
    hashInfo = hashs.get_object_hash(typehash)
    with open(filename, 'rb') as message:
        buf = message.read(16 * 1024)
        while len(buf) > 0:
            hashInfo.update(buf)
            buf = message.read(16 * 1024)
    hashFile = hashInfo.hexdigest()
    hashInfo = None
    return hashFile

def print_info(name, hash):
    print(f"{hash}  {name}")