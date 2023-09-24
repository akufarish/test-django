from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("add", views.add, name="add"),
    path("<int:id>", views.delete, name="delete"),
    path("update/<int:id>", views.updatePage, name="updatePage"),
    path("data/update/<int:id>", views.update, name="updatePage")
]