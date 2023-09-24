from django.db import models

# Create your models here.
class Murid(models.Model):
    nama = models.CharField(max_length=255)
    kelas = models.IntegerField()
    jurusan = models.CharField(max_length=255)