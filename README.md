# deepHash

Este programa tem o objetivo de identificar assinaturas maliciosas com a utilização de yara rules em sistemas Linux e Windows. Atualmente o programa está sendo desenvolvido na linguagem python versão 3.


# Dependências

O deepHash pode ser executado em sistemas Windows e Linux. O programa depende dos seguintes modulos python:

* yara-python
* pycryptodome
* pefile

Com o python versão 3 já instalado no sistema operacional basta executar o seguinte comando para instalar as dependências :

* python3 -m pip install .

ou

* pip3 install -r .

ou 

* make install

A instalação descrita acima não habilita todos os modulos do yara por padrão. Os modulos do yara podem ser utilizados na construção de rules. Caso algum modulo do yara-python não esteja disponível poderá ocorrer uma exceção de SintaxeError no momento da compilação da rule yara. Para habilitar todas as funcionalidades disponíveis do yara-python é preciso instalar as seguintes dependências, caso as libs não estejam disponíveis: 

* libjansson-dev
* libssl-dev
* libmagic-dev

Em seguida a instalação do pacote yara-python deve ser feita com o seguinte comando:

* pip3 install --global-option="build" --global-option="--enable-cuckoo" --global-option="--enable-magic" --global-option="--enable-dotnet" --global-option="--enable-dex" --global-option="--enable-dex" --global-option="--enable-macho" --global-option="--enable-profiling" yara-python

# Uso

O deepHash atualmente busca arquivos de forma recursiva em um diretório para gerar um hash do arquivo encontrado e validar se o arquivo possuí alguma assinatura maliciosa.

A execução do deepHash pode ser realizadas das seguintes formas:

Sem passagem de argumentos

* python3 deepHash.py

Informando qual o diretório onde a busca deve ser realizada

* python3 deepHash.py --dir DIR_ABSOLUTE_PATH

Informando qual o tipo de hash que deve ser gerado. Atualmente os tipos suportados são: MD5, SHA256 e SHA512

* python3 deepHash.py --type TYPE_HASH

Informando o nome do arquivo a ser analisado:

* python3 deepHash.py --file DIR_ABSOLUTE_PATH_FILE

Também é possível utilizar os parâmetros --dir e --type ou --file e --type simultaneamente