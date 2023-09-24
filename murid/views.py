from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.http import require_http_methods 
from .models import Murid
# Create your views here.
def index(request):
    murid = Murid.objects.all()
    return render(request, "index.html", {"murid": murid})

def __str__(self):
    return self.title

@require_http_methods("POST")
def add(request):
    nama = request.POST["nama"]
    kelas = request.POST["kelas"]
    jurusan = request.POST["jurusan"]
    murid = Murid(nama=nama, kelas=kelas, jurusan=jurusan)
    murid.save()
    return redirect("home")

def delete(request, id):
    murid = Murid.objects.get(id=id)
    murid.delete()
    return redirect("home")

def updatePage(request, id):
    murid = Murid.objects.get(id=id)
    return render(request, "update.html", {"murid": murid})

@require_http_methods("POST")
def update(request, id):
    nama = request.POST["nama"]
    kelas = request.POST["kelas"]
    jurusan = request.POST["jurusan"]
    murid = Murid.objects.get(id=id)
    murid.nama = nama
    murid.kelas = kelas
    murid.jurusan = jurusan
    murid.save()
    return redirect("home")