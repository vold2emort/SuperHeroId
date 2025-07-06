from django.shortcuts import render, redirect, get_object_or_404
from .models import SuperHeroes
from .forms import SuperheroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def home(request):
    return render(request, 'heroes/home.html')


@login_required
def hero_list(request):
    heroes = SuperHeroes.objects.all()
    return render(request, 'heroes/hero_list.html', {'heroes': heroes})


@login_required
def hero_detail(request, id):
    hero = get_object_or_404(SuperHeroes, id=id)
    return render(request, 'heroes/hero_detail.html', {'hero': hero})


@login_required
def add_hero(request):
    if request.method == 'POST':
        form = SuperheroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hero_list')
    else:
        form = SuperheroForm()
    return render(request, 'heroes/add_hero.html', {'form': form})


@login_required
def delete_hero(request, id):
    hero = get_object_or_404(SuperHeroes, id=id)
    hero.delete()
    return redirect('hero_list')


@login_required
def logout_view(request):
    return logout(request)