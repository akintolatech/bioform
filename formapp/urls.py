from . import views
from django.urls import path, include

app_name = "index"

urlpatterns = [
    path('', views.index, name="index"),
    path('bio-data/', views.bio_data_form, name="bio_data_form"),
]
