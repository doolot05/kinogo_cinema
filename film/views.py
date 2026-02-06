from django.shortcuts import render, get_object_or_404
from film.models import Film, Category

def base(request):
    categories = Category.objects.all()
    films = Film.objects.all()
    return render(request, "base.html", {
        'categories': categories,
        'films': films
    })

def films_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    films = Film.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, "base.html", {
        'films': films,
        'categories': categories,
        'category': category
    })

def film_detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    return render(request, "films/film_detail.html", {'film': film})

def film_list(request):
    films = Film.objects.all()
    return render(request, "films/film_list.html", {'films': films})
