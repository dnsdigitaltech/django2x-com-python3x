from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm
import datetime
# Create your views here.
def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None) # Verifica se já tem conteúdo ou nao

    if form.is_valid():
        form.save()
        return redirect('url_listagem') # Ao salvar retornará para listagem

    data['form'] = form
    return render(request, 'contas/form.html', data)

def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk) # pega o objeto específico
    form = TransacaoForm(request.POST or None, instance=transacao) # para para o form a instância do objeto

    if form.is_valid():
        form.save()
        return redirect('url_listagem') # Ao salvar retornará para listagem

    data['form'] = form
    data['transacao'] = transacao # enviar objeto para ser deletado
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk) # pega o objeto específico
    transacao.delete()
    return redirect('url_listagem') # Ao deletar retornará para listagem
