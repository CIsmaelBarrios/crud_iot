from django.db import models

class Crudiot(models.Model):
    nombre=models.CharField(max_length=100)
    correo=models.EmailField()
    mensaje=models.TextField()
    telefono=models.CharField(max_length=100)
