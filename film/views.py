from django.http import HttpResponse
from django.shortcuts import render
from film.models import Film

#select*from film;
#Film.objects.create()

#select*from film where id= '2';
#Film.objects.get(id=2) == возвращает 1 объект
#select * from film where (name = 'laptop')
#select*from product $Like where name = 'laptop' and year '1000';
#Film.objects.filter(name__icontains='laptop', year=1000)
#Film.objects.create(name='laptop', year=1000, description='laptop')

#Film.objects.update(price=1000) - изменение всех продуктов

#Film.objects.delete()




# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def film_list(request):
    films = Film.objects.all()
    return render(request, "films/film_list.html", context={'films': films})


def film_detail(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request, "films/film_detail.html", context={'film': film})



def base(request):
    return render(request, "base.html")

