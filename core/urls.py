from django.urls import path
from . import views

urlpatterns = [
    path('import-csv/', views.import_csv),
    path('', views.index),
]