from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # /bible/1
    path("<int:skibidi>/", views.mango, name="wers"),
]
lista = ["test"]
lista.remove("test")