from django.urls import path
from siteapp import views

app_name = 'siteapp'

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('patches', views.PatchesListView.as_view(), name='patch_list')
]
