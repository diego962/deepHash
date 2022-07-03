import Crypto
from Crypto.Hash import *

objectHashs = {
    "MD5": Crypto.Hash.MD5,
    "SHA256": Crypto.Hash.SHA256,
    "SHA512": Crypto.Hash.SHA512
}


def get_object_hash(typeHash="MD5"):

    return objectHashs[typeHash].new()
