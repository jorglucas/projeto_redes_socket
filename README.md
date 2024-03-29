## Projeto Redes Socket

Este projeto em Python utiliza web socket para criar uma relação direta entre clientes e servidor. O principal objetivo é possibilitar a visualização, o envio e a exclusão de arquivos de um servidor.


## Funcionalidades do Sistema

|   Status       |                 Pincipais Funcionalidades     |
| :-----------:  | :-------------------------------------------: |
|       ✅       | Listar arquivos existentes no servidor        |
|       ✅       | Enviar arquivos para o servidor               |
|       ✅       | Apagar arquivos para o servidor (com senha padrão: 1234)|
|       ✅       | Sair do servidor                              |
|       ✅       | Tratamento de alguns erros comuns             |

<br/>

|   Status       |                 Poderia ter sido implementado |
| :-----------:  | :-------------------------------------------: |
|       ❌       | Tratamento de alguns erros no lado do servidor|
|       ❌       | Monitoramento de dados recebidos e enviados pelo servidor|
|       ❌       |   Baixar arquivos do servidor                 |


## Funções que poderiam ser implementadas 

Algumas funções poderiam ser implementadas para deixar a aplicação ainda mais completa, como por exemplo: o tratamento de alguns erros no lado do servidor, monitoramento de dados enviados e recebidos pelo servidor, possibilitar o download de arquivos pelo cliente, mostrar o tamanho de cada arquivo para o cliente na parte de listagem. 

## Dificuldades encontradas no desenvolvimento do projeto

Algumas dificuldades foram encontradas durante o desenvolvimento da aplicação, como por exemplo: o uso de timeOut para o desligamento do servidor, download de arquivos por parte do cliente, etc.

## Requisitos do Sistema

Para rodar o projeto disponível neste repositório, é necessário instalar os seguintes programas em seu computador:

- `Python3` (versão 3.9.0 ou superior) - [link](https://www.python.org/downloads/)

## Instalação do Python3

O processo de instalação do Python3 é bem simples, basta ir ao link fornecido acima, baixar a versão mais adequada para o seu sistema e seguir os passos existentes durante a instalação. Lembrando de adicionar o Pyhton nas variáveis de ambiente.

## Executando o servidor

Após o python3 ser baixado e instalado, faça o download desse repositório e entre na pasta de destino: `[...]/projeto_redes_socket` e execute o arquivo `[...]/projeto_redes_socket/servidor.py`, usando o seguinte comando na raiz do projeto: `python3 servidor.py` e em seguida você deve digitar qual a porta você quer abrir para conexões. Por padrão, o IP é definido como 'localhost' tanto no servidor quanto no cliente.

## Executando o cliente

Em outro terminal, no diretório onde está o `client.py` digite `python3 client.py`para executar o cliente. Assim como no servidor, no cliente também é necessário informar em qual porta você deseja tentar conexão e essa porta deve ser a mesma que foi definida no servidor.
O `client.py` pode ser executado quantas vezes você quiser, já que no projeto foi utilizado Threads, que permite a execução de vários processos simultâneos.

## Utilizando o projeto...

Para receber as primeiras instruções digite `ajuda` e tecle `ENTER` para enviar.
Caso o comando esteja correto você receberá uma lista de comandos, como usá-los e qual sua função.
Obs. 1: Para o comando `enviar` deve digitar o caminho onde se encontra o arquivo desejado. Para nosso exemplo, os arquivos estão na pasta `client_files`, logo o comando deverá ser `enviar client_files/teste.txt`
Obs. 2: Para o comando `deletar`, você deve digitar o nome do arquivo que deseja excluir no servidor e a senha de administrador (1234), logo o comando deverá ser `deletar teste.txt 1234`.


## Dupla do projeto:

Jhonata Tenório e Jorge Lucas

