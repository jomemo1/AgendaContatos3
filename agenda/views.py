from django.shortcuts import render, redirect
from .models import Contato
from django.http import HttpResponse
from .forms import ContatoForm

def contato_lista(request):
    contatos = Contato.objects.all().order_by('nome')
    return render(
        request,
        'agenda/contato_lista.html',
        {'contatos': contatos}
    )

def contato_lista_http(request):
    contatos = Contato.objects.all().order_by('nome')
    return HttpResponse('''
                <h1>Lista de contatos</h1>
            ''')

def contato_criar(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:contato_lista')
    else:
        form = ContatoForm()
    return render(request, 'agenda/contato_form.html', {'form': form, 'titulo_pagina': 'Adicionar  Contato'})
