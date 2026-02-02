from django.db import models

# Create your models here.
#ORM Object Relational Mapping
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"




class Film(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    rating = models.FloatField(default=0, verbose_name="Рейтинг")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} -- {self.year}"


