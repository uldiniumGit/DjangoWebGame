from django.urls import path
from siteapp import views

app_name = 'siteapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('patchnotes/', views.patchnotes, name='patchnotes'),
]
