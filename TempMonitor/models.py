from django.db import models

class todo(models.Model):
    name = models.CharField(max_length=100)  # Nome da sala
    temperature = models.FloatField()  # Temperatura da sala
    data_e_hora = models.DateTimeField(auto_now_add=True)  # Data e hora da criação

class TipoSensor(models.Model):
    tipo = models.CharField(max_length=50)
    Sigla = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, blank=True, default='Sem descrição')

class Pavimento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)


class Orientacao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)


class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=10)
    id_pavimento = models.ForeignKey(Pavimento, on_delete=models.CASCADE)
    id_orientacao = models.ForeignKey(Orientacao, on_delete=models.CASCADE)
