É necessário tem estes 4 itens instalado em seu SO

- Python - Baixar no site https://www.python.org/downloads/
- Pip
- Django
- Pycharm ou VSCODE

Python

Testar se o python está instalado, basta abrir o terminal e digitar o seguinte comando:
python ou python3

Pip

Ver se o Pip está intalado, geralmente ja vem com o python
é necessário criar uma virtual env, pois é um isolamento que o python criará em sua aplicação evitando que 
interfira em outro projetos, criando um ambiente virtual para uma aplicação específica.

Para criar uma virtual env basta rodar o serguinte comando no terminal dentro do seu diretório python3 -m venv nome_da_sua_venv
python3 -m venv venv

para ativar sua venv basta digitar o seguinte comando
source  venv/bin/activate

Aparece (venv) desenv01@desenv01-Vostro-3583:~/Documentos/django2x-com-python3x$ no início do seu terminal, pois o pip deixa isolado

Se digitar pip o comando já funciona.

Django

para instalar o djando basta digitar o comando
pip install django

OBS: o pip é responsável por instalar, atualizar o django

Testando o django
com a venv ativada basta digitar os seguintes comandos em sequências
python
import django
django.VERSION

Para ver onde está instalado o django dentro da venv banta acessar
/home/desenv01/Documentos/django2x-com-python3x/venv/lib/python3.6/site-packages/django

Para criar o projeto basta digitar o seguuinte comando com a sua venv ativada
django-admin startproject controle_gastos

Você poderá ver que foi criado o projeto com todos arquivos de inicialização do django

Explicação dos arquivos:
__init__.py - que diser que este dir é considerado um pacote python
asgi.py - onde fica o core do sistema
settings.py - é o setup do nosso projeto
urls.py - Local onde ficará as urls do projeto
wsgi.py - endpoint da aplicação, não mexeremos neste aquivo
manager.py - arquivo utilitário, vai ajudar a gerenciar o projeto, criar banco de dados, migrações upser usuários, não precisa mexer.

