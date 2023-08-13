from django.urls import path
from siteapp import views
from django.contrib.auth.views import LogoutView

app_name = 'siteapp'

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('patches', views.PatchesListView.as_view(), name='patch_list'),
    path('registration', views.UserCreateView.as_view(), name='registration'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]
