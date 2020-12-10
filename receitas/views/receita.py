'''
Controls the list of receipts and the receipt page views
'''

from django.shortcuts import render, redirect, get_object_or_404
from receitas.models import Receita
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    '''
    Show the list of receipts
    '''

    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }

    return render(request, 'receitas/index.html', dados)


def receita(request, receita_id):
    '''
    Show the receipt page
    '''

    objeto_receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {
        'receita': objeto_receita
    }
    return render(request, 'receitas/receita.html', receita_a_exibir)


def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto = request.FILES['foto']

        user = get_object_or_404(User, pk=request.user.id)
        print(user)
        receita = Receita.objects.create(
            nome_receita=nome_receita,
            ingredientes=ingredientes,
            modo_preparo=modo_preparo,
            tempo_preparo=tempo_preparo,
            rendimento=rendimento,
            categoria=categoria,
            pessoa=user,
            foto=foto
        )
        receita.save()
        return redirect('dashboard')

    return render(request, 'receitas/cria_receita.html')


def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')


def edita_receita(request, receita_id):
    objeto_receita = get_object_or_404(Receita, pk=receita_id)
    receita = { 'receita': objeto_receita }
    return render(request, 'receitas/edita_receita.html', receita)


def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        objeto_receita = Receita.objects.get(pk=receita_id)

        objeto_receita.nome_receita = request.POST['nome_receita']
        objeto_receita.ingredientes = request.POST['ingredientes']
        objeto_receita.modo_preparo = request.POST['modo_preparo']
        objeto_receita.tempo_preparo = request.POST['tempo_preparo']
        objeto_receita.rendimento = request.POST['rendimento']
        objeto_receita.categoria = request.POST['categoria']
        if 'foto' in request.FILES:
            objeto_receita.foto = request.FILES['foto']

        objeto_receita.save()

        return redirect('dashboard')

    return redirect('edita_receita')
