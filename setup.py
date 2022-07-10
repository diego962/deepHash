import os

from setuptools import find_packages, setup


def read(*paths):
    rootpah = os.path.dirname(__file__)
    filepath = os.path.join(rootpah, *paths)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"'))
    ]


setup(
    name="deepHash",
    version="0.3.0",
    description="""
        O deepHash faz o calculo de hash de arquivos em sistemas Linux e
        Windows e verifica se o arquivo é malicioso usando yara rules
    """,
    author="Diego Lopes",
    packages=find_packages(),
    package_data={
        "dph.yara-rules": ["*.yar"],
        "dph.yara-rules.malware": ["*.yar"],
        "dph.yara-rules.pdf": ["*.yar"],
        "dph.yara-rules.malware.opblockbuster": ["*.yara"],
    },
    entry_points={"console_scripts": ["dph = dph.__main__:main"]},
    install_requires=read_requirements("requirements.txt"),
)
