from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Jossue", views.Jossue, name="Jossue"),
    path ("<str:name>", views.greet, name="greet")
]
