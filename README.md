# Project

Este projeto tem o objetivo de identificar assinaturas maliciosas com a utilização de yara rules em sistemas Linux e Windows. O projeto desenvolvido na linguagem python versão 3.


# Requirements

O deepHash pode ser executado em sistemas Windows e Linux. O projeto depende dos seguintes pacotes python:

* yara-python
* pycryptodome

Com o python versão 3 já instalado no sistema operacional basta executar o seguinte comando para instalar as dependências :

* python3 -m pip install -r requirements.txt

ou

* pip3 install -r requirements.txt

A instalação descrita acima não habilita todos os modulos do yara por padrão. Os modulos do yara podem ser utilizados na construção de rules, caso o modulo não esteja disponível podera ocorrer uma exceção de SintaxeError no momento da compilação da rule yara. Para habilitar todas as funcionalidades disponiveis do yara é preciso instalar as seguintes dependências, caso as libs não estejam disponíveis: 

* libjansson-dev
* libssl-dev
* libmagic-dev

Em seguida a instalação do pacote yara-python deve ser feita com o seguinte comando:

* pip3 install --global-option="build" --global-option="--enable-cuckoo" --global-option="--enable-magic" --global-option="--enable-dotnet" --global-option="--enable-dex" --global-option="--enable-dex" --global-option="--enable-macho" --global-option="--enable-profiling" yara-python

# Usage

O deepHash atualmente busca arquivos de forma recursiva em um diretório para gerar um hash do arquivo encontrado e validar se o arquivo possuí alguma assinatura maliciosa utilizando rules yara para detectar essas assinaturas.

A execução do deepHash pode ser des três formas:

Sem passagem de argumentos

* python3 deepHash.py

Informando qual o diretório onde a busca deve ser realizar

* python3 deepHash.py --dir DIR_ABSOLUTE_PATH

Informando qual o tipo hash que deve ser gerado. Atualmente os tipos suportados são: MD5, SHA256 e SHA512

* python3 deepHash.py --type TYPE_HASH

Também é possível utilizar os parâmetros --dir e --type simultaneamente
