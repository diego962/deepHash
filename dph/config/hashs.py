from Crypto.Hash import MD5, SHA256, SHA512

objectHashs = {
    "MD5": MD5,
    "SHA256": SHA256,
    "SHA512": SHA512,
}


def get_object_hash(typeHash="MD5"):

    return objectHashs[typeHash].new()
