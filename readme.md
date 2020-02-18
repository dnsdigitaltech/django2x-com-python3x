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

Primeira App
O django é baseado em Apps então vamos criar a primeira App digite no terminal da sua aplicação
python manage.py startapp contas
A App foi criada com os seguintes arquivos e diretório
/migratios
__init__.py - arquivo que informa que este dir e python
admin.py - registrar a aplicação debtro do nosso admin
apps.py - definiremos nossa app
models.py - definiremos nossos models
tests.py - usado para testes
views.py - e as views

OBS: quando criamos nossa App primeira coisa a ser feita é registrar nossa App no nosso settings

INSTALLED_APPS = [
    ........
    'contas',
]

Criar nosso banco de dados com o seguinte comando criará o arquivo sqlite3
python manage.py migrate

criou o banco e estas tabelas:
Apply all migrations: admin, auth, contenttypes, sessions

Executando nossa aplicação local com o seguinte comando
python manage.py runserver

Criando o super usuario para logar na aplicação
python manage.py createsuperuser

CRIANDO URL E VIEW 
Para criar a url basta importá de uma view específica
from contas.views import home
urlpatterns = [
    path('contas/', home)
]

As views são pedaços de códigos que ficam dentro do arquivos wiew.py (funções) direcionada a uma página específica

Toda view recebe requests como parâmetros e terá um return HttpResponse()
def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

Como retornar um templates
Ao invés de responder com return HttpResponse(), basta responder com render()
é necessário criar um diretório chamado templates/contas e dentro o arquivo home.html

def home(request):
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'contas/home.html')

Models
São basicamente cada campos da sua base de dados definidas em uma classe
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

Depois que você cria a model basta rodar a migrations e neste caso vamos criar com o seguinte código
python manage.py makemigrations

Criando um arquivo migrations dentro do dir migrations.
controle_gastos/contas/migrations/0001_initial.py

Uma vex que criou o arquivo migrations agora basta criar a tabela no banco com o seguinte comando
python manage.py migrate

Como ver de foi criado com sucesso a minha tabela? Basta ir no admin.py e registra sua model lá, sem precisar escreve grande linha de código.

Basta rodar o server 

python manage.py runserver

Basta ir no seu admin e verifique que já esiste a categoria lá
http://127.0.0.1:8000/admin/

Model Transação com conceito de chave estrangeira
class Transação(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField()

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

E registra no admin

Class Meta muda o nome da classe meta define o nome de plural da classe x

    class Meta:
        verbose_name_plural = "Transacoes"

    definir como serpa exibido os dados de cada objetos na tela
    def __str__(self):
        return self.descricao