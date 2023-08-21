from django.urls import path
from siteapp import views
from django.contrib.auth.views import LogoutView

app_name = 'siteapp'

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('registration', views.UserCreateView.as_view(), name='registration'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('key1', views.GetForgeKeyView.as_view(), name='key1'),
    path('key2', views.GetGreenhouseKeyView.as_view(), name='key2'),
    path('key3', views.GetStonesKeyView.as_view(), name='key3'),
    path('key4', views.GetLoftKeyView.as_view(), name='key4'),
    path('key5', views.GetKitchenKeyView.as_view(), name='key5'),
    path('key6', views.GetFishermanKeyView.as_view(), name='key6'),
    path('getmaster', views.GetMasterKeyView.as_view(), name='getmaster'),
    path('losemaster', views.LoseMasterKeyView.as_view(), name='losemaster'),
    path('daytwo', views.DayTwoView.as_view(), name='daytwo'),
    path('patches', views.PatchesListView.as_view(), name='patch_list'),
    path('stones', views.StonesView.as_view(), name='stones'),
    path('greenhouse', views.GreenHouseView.as_view(), name='greenhouse'),
    path('hall', views.HallView.as_view(), name='hall'),
    path('kitchen', views.KitchenView.as_view(), name='kitchen'),
    path('loft', views.LoftView.as_view(), name='loft'),
    path('fisherman', views.FishermanView.as_view(), name='fisherman'),
    path('forge', views.ForgeView.as_view(), name='forge'),
]
