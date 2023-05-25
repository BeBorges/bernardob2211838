from django.shortcuts import render, redirect, get_object_or_404
from .models import Curiosity, TopScorer
from .forms import CuriosityForm, TopScorerForm

def home(request):
    # Renderiza a página inicial (home.html)
    return render(request, 'home.html')

def top_scorers(request):
    # Obtém todos os melhores pontuadores do banco de dados
    top_scorers = TopScorer.objects.all()
    # Renderiza a página de melhores pontuadores (top_scorers.html) e passa os melhores pontuadores para o template
    return render(request, 'top_scorers.html', {'top_scorers': top_scorers})

def curiosities(request):
    # Obtém todas as curiosidades do banco de dados
    curiosities = Curiosity.objects.all()
    # Renderiza a página de curiosidades (curiosities.html) e passa as curiosidades para o template
    return render(request, 'curiosities.html', {'curiosities': curiosities})

def add_curiosity(request):
    # Cria um formulário vazio para adicionar uma nova curiosidade
    form = CuriosityForm()
    if request.method == 'POST':
        # Se a requisição for do tipo POST, cria um formulário preenchido com os dados enviados
        form = CuriosityForm(request.POST)
        if form.is_valid():
            # Se o formulário for válido, salva os dados no banco de dados
            form.save()
            # Redireciona para a página inicial
            return redirect("home")
    # Renderiza a página de adicionar curiosidade (add_curiosity.html) e passa o formulário para o template
    return render(request, 'add_curiosity.html', {'form': form})

def add_top_scorer(request):
    # Cria um formulário vazio para adicionar um novo melhor pontuador
    form = TopScorerForm()
    if request.method == 'POST':
        # Se a requisição for do tipo POST, cria um formulário preenchido com os dados enviados
        form = TopScorerForm(request.POST)
        if form.is_valid():
            # Se o formulário for válido, salva os dados no banco de dados
            form.save()
            # Redireciona para a página inicial
            return redirect('home')
    # Renderiza a página de adicionar melhor pontuador (add_top_scorer.html) e passa o formulário para o template
    return render(request, 'add_top_scorer.html', {'form': form})

def edit_curiosity(request, pk):
    # Obtém a curiosidade com o ID especificado (pk) do banco de dados
    curiosity = get_object_or_404(Curiosity, pk=pk)
    # Cria um formulário preenchido com os dados da curiosidade
    form = CuriosityForm(instance=curiosity)

    if request.method == 'POST':
        # Se a requisição for do tipo POST, cria um formulário preenchido com os dados enviados
        form = CuriosityForm(request.POST, instance=curiosity)
        if form.is_valid():
            # Se o formulário for válido, salva os dados no banco de dados
            form.save()
            # Redireciona para a página inicial
            return redirect('home')

    # Renderiza a página de editar curiosidade
