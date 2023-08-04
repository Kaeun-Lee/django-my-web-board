from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    path("", views.index, name="home"),
    path("<int:board_id>", views.detail, name="detail"),
]