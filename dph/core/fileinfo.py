import pefile

from dph.config.section import SectionName


def exists_invalid_section(file):
    try:
        for section in file.sections:
            name_section = section.Name.decode().rstrip("\x00")
            SectionName(name_section)
        return False
    except ValueError:
        return True


def is_malware(filename):
    try:
        file = pefile.PE(filename)
        if exists_invalid_section(file):
            return True
        elif file.OPTIONAL_HEADER.SizeOfInitializedData == 0:
            return True
        elif (
            file.OPTIONAL_HEADER.DllCharacteristics == 0
            and file.OPTIONAL_HEADER.MajorImageVersion == 0
            and file.OPTIONAL_HEADER.CheckSum == 0
        ):
            return True
        else:
            return False
    except pefile.PEFormatError:
        return False
