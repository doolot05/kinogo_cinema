
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from film import views
from film.views import (
    base,
    film_create,
    film_list,
    film_detail,
)

from users.views import (
     register, login_user, logout_user,
)
users = [
    path('register/', register),
    path('login/', login_user),
    path('logout/', logout_user),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('films/', views.film_list, name='film_list'),
    path('films/<int:film_id>/', views.film_detail, name='film_detail'),
    path("film_create/", film_create),
    *users
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
