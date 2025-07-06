from django.shortcuts import render, redirect, get_object_or_404
from .models import SuperHeroes
from .forms import SuperheroForm

def home(request):
    return render(request, 'heroes/home.html')

def hero_list(request):
    heroes = SuperHeroes.objects.all()
    return render(request, 'heroes/hero_list.html', {'heroes': heroes})

def hero_detail(request, id):
    hero = get_object_or_404(SuperHeroes, id=id)
    return render(request, 'heroes/hero_detail.html', {'hero': hero})

def add_hero(request):
    if request.method == 'POST':
        form = SuperheroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hero_list')
    else:
        form = SuperheroForm()
    return render(request, 'heroes/add_hero.html', {'form': form})

def delete_hero(request, id):
    hero = get_object_or_404(SuperHeroes, id=id)
    hero.delete()
    return redirect('hero_list')
