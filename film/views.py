from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateFilmForm
from .models import Film, Category

def base(request):
    if request.method == "GET":
        categories = Category.objects.all()
        films = Film.objects.all()
    return render(request, "base.html", {
        'categories': categories,
        'films': films
    })



def film_detail(request, film_id):
    if request.method == "GET":
        film = get_object_or_404(Film, id=film_id)
        return render(request, "films/film_detail.html", {'film': film})

@login_required(login_url="/login/")
def film_create(request):
    if request.method == "GET":
        forms = CreateFilmForm()
        return render(request, "films/film_create.html", context={'forms': forms})
    elif request.method == "POST":
        forms = CreateFilmForm(request.POST, request.FILES)
        if forms.is_valid():
            Film.objects.create(
                name=forms.cleaned_data.get("name"),
                description=forms.cleaned_data.get("description"),
                year=forms.cleaned_data.get("year"),
                image=forms.cleaned_data.get("image"),

             )
            return redirect("/films/")
        form = CreateFilmForm()
        return render(request, "films/film_create.html", {'form': form})


@login_required(login_url="/login/")
def film_list(request):
    if request.method == "GET":
        films = Film.objects.all()
        category_id = request.GET.get("category_id")
        if category_id:
            films = Film.objects.filter(category_id=category_id)
        return render(request, "films/film_list.html", {'films': films})
