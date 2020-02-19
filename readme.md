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
    djadjango.VERSIONngo.VERSION

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

Depois rode os seguites comandos

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

E registra no admin

Class Meta muda o nome da classe meta define o nome de plural da classe x

    class Meta:
        verbose_name_plural = "Transacoes"

definir como será exibido os dados de cada objetos na tela

    def __str__(self):
        return self.descricao

Enviando dicionário de informações para para o templates basta envirar na view

    def home(request):
        data = {}
        data['transacoes'] = ['t1', 't2', 't3']
        data['now'] = datetime.datetime.now()
        #html = "<html><body>It is now %s.</body></html>" % now
        return render(request, 'contas/home.html', data)

No template basta pegar os valores variáveis conforme mostrado abaixo:

    <p>Agora são: {{now}}</p>
    <h5>Exibindo todos os dados da lista</h5>
    <ul>
        {% for transacao in transacoes %}
            <li>{{transacao}}</li>
        {%endfor%}
    </ul>
    <h5>Exibindo dados da lista através de uma condição</h5>
    <ul>
        {% for transacao in transacoes %}
            {% if transacao == 't1' %}
                <li><b>{{transacao}}</b></li>
            {% else %}
                <li>{{transacao}}</li>
            {% endif %}
        {% endfor %}
    </ul>


CRUD ['create','read','update','delete']

Read - fazendo a leitura dos dados que estão na base

Primeira coisa a fazer é chamar o importe do model na view

    from .models import Transacao

Depois cria uma classe para acessar todo conteúdo do banco

    def listagem(request):
        data = {}
        data['transacoes'] = Transacao.objects.all()
        return render(request, 'contas/listagem.html', data)

Create - fazendo a inserção dos dados  na base

Formulário baseado em um Model (ModelForm)
Primeiro a fazer pe criar um arquivo chamado forms.py, deposi basta colcoar os metadados dos campos do seu form conforma visualisado abaixo:

    from django.forms import ModelForm
    from .models import Transacao

    class TransacaoForm(ModelForm):
        class Meta:
            model = Transacao
            fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']

OBS: você poderá trabalhar com form html manuais, porém esta é uma facilidade que o django nos fornece.
Basta cria ums função na sua view importando seu form como no exemplo abaixo:

    from .form import TransacaoForm

    def nova_transacao(request):
        data = {}
        form = TransacaoForm(request.POST or None) # Verifica se já tem conteúdo ou nao

        if form.is_valid():
            form.save()
            return listagem(request) # Ao saçvar retornará para listagem

        data['form'] = form
        return render(request, 'contas/form.html', data)

Não esqueça de adicionar a url

    from contas.views import home, listagem, nova_transacao

    urlpatterns = [
        .....
        path('nova/', nova_transacao, name='url_nova'),
    ]

No seu template poderá usar seu formulário, não esquecedo com csrf_token

    <form method="POST">
        {% csrf_token %}

        {{ form.as_p }}

        <button type="submit">salvar</button>
    </form>

Update - fazendo a atualização dos dados que estão na base

Agora á necessário criar uma url diferente, que ajude a encontrar o objeto certo no banco de dados, precisamos passar o id do objeto via paramêtro para localizá-lo na base.

Nosso método receberá um parâmetro o mais que é a pk

A view ficará assim:

    def update(request, pk):
        data = {}
        transacao = Transacao.objects.get(pk=pk) # pega o objeto específico
        form = TransacaoForm(request.POST or None, instance=transacao) # para para o form a instância do objeto

        if form.is_valid():
            form.save()
            return redirect('url_listagem') # Ao salvar retornará para listagem

        data['form'] = form
        return render(request, 'contas/form.html', data)

O template listamgem.html ficará assim

    <h1>Listagem</h1>
    <ul>
        {% for transacao in transacoes %}
            <li>
                <a href="{% url 'url_update' transacao.id %}">
                    {{ transacao.id }} - {{ transacao.descricao }} - {{ transacao.data }} - {{ transacao.valor }} - {{ transacao.categoria }}
                </a>
            </li>
        {% endfor %}
    </ul>
    <a href="{% url 'url_nova' %}">Novo</a>

A url ficará assim

    from django.contrib import admin
    from django.urls import path
    from contas.views import home, listagem, nova_transacao, update

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', listagem, name='url_listagem'),
        path('nova/', nova_transacao, name='url_nova'),
        path('update/<int:pk>/', update, name='url_update'),
        path('home/', home)
    ]

Delete - ecluindo dados que estão na base

Será necessário passar o id assim como no updade

