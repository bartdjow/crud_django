from django.db import models
from datetime import date

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    data_de_nascimento = models.DateField()
    
    def __str__(self):
        return self.nome