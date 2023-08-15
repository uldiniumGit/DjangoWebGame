from django.urls import path
from siteapp import views
from django.contrib.auth.views import LogoutView

app_name = 'siteapp'

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('patches', views.PatchesListView.as_view(), name='patch_list'),
    path('stones', views.StonesView.as_view(), name='stones'),
    path('greenhouse', views.GreenHouseView.as_view(), name='greenhouse'),
    path('registration', views.UserCreateView.as_view(), name='registration'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('key1', views.GetKeyView.as_view(), name='key1'),
    path('key2', views.LoseKeyView.as_view(), name='key2'),
]
