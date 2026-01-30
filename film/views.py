from django.http import HttpResponse
from django.shortcuts import render
from film.models import Film

#Film.objects.create()
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def film_list(request):
    films = Film.objects.all()
    return render(request, 'film_list.html', context={'films': films})
