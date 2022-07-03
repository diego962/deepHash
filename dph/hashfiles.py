from dph.config import osinfo
from dph.config import hashs
from dph.log import log
from dph.fileinfo import is_malware
from gc import collect
from time import sleep
import yara
import argparse

log = log.get_logger()

rules = yara.compile(filepath=osinfo.which_dirname(__file__) + "/yara-rules/rules.yar")
dir_format = '\\' if (osinfo.which_os() == "Windows") else '/'


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', dest="type")
    parser.add_argument('--dir', dest="dir")
    parser.add_argument('--file', dest="filename")

    arguments = parser.parse_args()

    typeHash = arguments.type.upper() if (arguments.type) else "MD5"
    directory = arguments.dir if (arguments.dir) else (osinfo.which_path())

    if (arguments.filename):
        (hash_file, matches, is_malicious) = calculate_hash(arguments.filename, typeHash)
        print_info(hash_file, arguments.filename, matches, is_malicious)
    else:
        deep_hash(directory, typehash=typeHash)


def deep_hash(directory, typehash=""):
    files = osinfo.ls_dir(directory) if (osinfo.is_dir(directory)) else [directory]

    for file in files:
        if (osinfo.is_file(directory + dir_format + file)):
            (hash_file, matches, is_malicious) = calculate_hash(directory + "/" + file, typehash)
            print_info(directory + dir_format + file, hash_file, matches, is_malicious)
            collect()

        if (osinfo.is_dir(directory + dir_format + file)):
            deep_hash(directory + dir_format + file, typehash=typehash)
        sleep(0.5)


def calculate_hash(filename, typehash):
    hashInfo = hashs.get_object_hash(typehash)
    is_malicious = is_malware(filename)
    matches = None

    with open(filename, 'rb') as message:
        matches = rules.match(data=message.read())

        message.seek(0)

        buf = message.read(16 * 1024)
        while len(buf) > 0:
            hashInfo.update(buf)
            buf = message.read(16 * 1024)
    hashFile = hashInfo.hexdigest()
    hashInfo = None
    return (hashFile, matches, is_malicious)


def print_info(name, hash, match, is_malicious):
    print("---------------------------------------------")
    print("HASH:\t{0}\nFILE:\t{1}\nYARA RULES:\t{2}\nIS MALWRE:\t{3}\n".format(hash, name, match, is_malicious))
    print("---------------------------------------------")

    log.setLevel("INFO")
    log.info("""
    ---------------------------------------------
    \tHASH:\t{0}\n\tFILE:\t{1}\n\tYARA RULES:\t{2}\n\tIS MALWRE:\t{3}\n
    ---------------------------------------------
    """.format(hash, name, match, is_malicious)
    )
