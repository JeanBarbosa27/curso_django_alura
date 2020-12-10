"""Controla o CRUD completo da receita"""

from receitas.models import Receita
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, Page
from alura_receita.settings import ITEMS_PER_PAGE


def index(request):
    """Exibe a lista de receitas publicadas na aplicação"""

    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    #TODO: O paginador poderia ser um serviço, já que está sendo usado no dashboard também
    paginador = Paginator(receitas, ITEMS_PER_PAGE)
    pagina = request.GET.get('page')
    receitas_paginadas = paginador.get_page(pagina)

    dados = {
        'receitas': receitas_paginadas
    }

    return render(request, 'receitas/index.html', dados)


def receita(request, receita_id):
    """Exibe as informações da receita selecionada"""

    objeto_receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {
        'receita': objeto_receita
    }
    return render(request, 'receitas/receita.html', receita_a_exibir)


def cria_receita(request):
    """Exibe a página de criar receita e salva uma nova receita no banco"""

    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto = request.FILES['foto']

        user = get_object_or_404(User, pk=request.user.id)
        nova_receita = Receita.objects.create(
            nome_receita=nome_receita,
            ingredientes=ingredientes,
            modo_preparo=modo_preparo,
            tempo_preparo=tempo_preparo,
            rendimento=rendimento,
            categoria=categoria,
            pessoa=user,
            foto=foto
        )
        nova_receita.save()

        return redirect('dashboard')

    return render(request, 'receitas/cria_receita.html')


def deleta_receita(request, receita_id):
    """Deleta a receita que foi selecionada no botão deletar da lista"""

    receita_selecionada = get_object_or_404(Receita, pk=receita_id)
    receita_selecionada.delete()
    return redirect('dashboard')


def edita_receita(request, receita_id):
    """Exibe página com os dados da receita, com um formulário para edição"""

    objeto_receita = get_object_or_404(Receita, pk=receita_id)
    receita = { 'receita': objeto_receita }
    return render(request, 'receitas/edita_receita.html', receita)


def atualiza_receita(request):
    """Recebe os dados do formulário de edição e salva as alterações no banco"""

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
