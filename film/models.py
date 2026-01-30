from django.db import models

# Create your models here.
#ORM Object Relational Mapping
class Film(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    rating = models.FloatField(default=0, verbose_name="Рейтинг")
    created_at = models.DateTimeField(auto_now_add=True)

