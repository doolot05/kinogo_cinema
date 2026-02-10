from django.contrib import admin
from film.models import Film, Category, Genre
# Register your models here.


admin.site.register(Category)
admin.site.register(Genre)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'category', 'created_at', 'update_at')
    list_filter = ('category',)

