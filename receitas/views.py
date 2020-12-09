'''
Controls the list of receipts and the receipt page views
'''

from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita


def index(request):
    '''
    Show the list of receipts
    '''

    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }

    return render(request, 'index.html', dados)


def receita(request, receita_id):
    '''
    Show the receipt page
    '''

    objeto_receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {
        'receita': objeto_receita
    }
    return render(request, 'receita.html', receita_a_exibir)


def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']

        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)
