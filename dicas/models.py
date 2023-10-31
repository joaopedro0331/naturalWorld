from django.db import models
from accounts.models import Usuario
# Create your models here.

class Dicas(models.Model):
    descricao = models.TextField()
    empresa = models.ForeignKey(Usuario, related_name=("Dicas"), on_delete=models.CASCADE)