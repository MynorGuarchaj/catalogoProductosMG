from django.db import models

# Create your models here.
class tareas(models.Model):
    codigo = models.IntegerChoices(max),
    descripcion = models.TextField (max_length=200),
    cantidad = models.IntegerChoices(max),
    precio = models.IntegerChoices(max),
    categoria =  models.TextField (max_length=200),
    descCategoria =  models.TextField (max_length=200),
