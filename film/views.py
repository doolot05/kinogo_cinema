
from django.shortcuts import render, get_object_or_404, redirect
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

def film_create(request):
    if request.method == "GET":
        return render(request, "films/film_create.html")
    elif request.method == "POST":
        print(request.POST)
        Film.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            year=request.POST.get("year"),
            image=request.FILES.get("image"),

        )
        return redirect("/films/")




def film_list(request):
    if request.method == "GET":
        films = Film.objects.all()
        category_id = request.GET.get("category_id")
        if category_id:
            films = Film.objects.filter(category_id=category_id)
        return render(request, "films/film_list.html", {'films': films})
