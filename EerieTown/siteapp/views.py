from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, View
from .models import PatchNote, GameUser
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponse, HttpResponseRedirect


# Ключи
class GetMasterKeyView(View):
    def get(self, request):
        user = request.user
        setattr(user, 'has_forge_key', True)
        setattr(user, 'has_greenhouse_key', True)
        setattr(user, 'has_stones_key', True)
        setattr(user, 'has_loft_key', True)
        setattr(user, 'has_kitchen_key', True)
        setattr(user, 'has_fisherman_key', True)
        user.save()
        return redirect('siteapp:index')


class LoseMasterKeyView(View):
    def get(self, request):
        user = request.user
        setattr(user, 'has_forge_key', False)
        setattr(user, 'has_greenhouse_key', False)
        setattr(user, 'has_stones_key', False)
        setattr(user, 'has_loft_key', False)
        setattr(user, 'has_kitchen_key', False)
        setattr(user, 'has_fisherman_key', False)
        setattr(user, 'day_two', False)
        setattr(user, 'day_three', False)
        setattr(user, 'end', False)
        user.save()
        return redirect('siteapp:index')


class GetForgeKeyView(View):
    def get(self, request):
        user = request.user
        setattr(user, 'has_forge_key', True)
        user.save()
        return redirect('siteapp:index')


class GetGreenhouseKeyView(View):
    def get(self, request):
        user = request.user
        setattr(user, 'has_greenhouse_key', True)
        user.save()
        return redirect('siteapp:index')


class GetStonesKeyView(View):
    def get(self, request):
        user = request.user
        setattr(user, 'has_stones_key', True)
        user.save()
        return redirect('siteapp:fisherman')


class GetLoftKeyView(View):
    def get(self, request):
        user = request.user
        setattr(user, 'has_loft_key', True)
        user.save()
        return redirect('siteapp:hall')


class GetKitchenKeyView(View):
    def get(self, request):
        user = request.user
        setattr(user, 'has_kitchen_key', True)
        user.save()
        return redirect('siteapp:index')


class GetFishermanKeyView(View):
    def get(self, request):
        user = request.user
        setattr(user, 'has_fisherman_key', True)
        user.save()
        return redirect('siteapp:index')


# Смена дня
class DayTwoView(View):
    def get(self, request):
        user = request.user
        setattr(user, 'day_two', True)
        user.save()
        return redirect('siteapp:loft')


class DayThreeView(View):
    def get(self, request):
        user = request.user
        setattr(user, 'day_three', True)
        user.save()
        return redirect('siteapp:greenhouse')


# Конец
class EndView(View):
    def get(self, request):
        user = request.user
        setattr(user, 'end', True)
        user.save()
        return redirect('siteapp:square')


# Вспомогательные страницы
class UserCreateView(CreateView):
    model = GameUser
    template_name = 'siteapp/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('siteapp:login')


class UserLoginView(LoginView):
    template_name = 'siteapp/login.html'
    authentication_form = LoginForm


class PatchesListView(ListView):
    model = PatchNote
    template_name = 'siteapp/patch_list.html'

    def get_queryset(self):
        return super(PatchesListView, self).get_queryset().order_by('-id')


# Карта и локации
class MainView(TemplateView):
    template_name = 'siteapp/index.html'


class SquareView(TemplateView):
    template_name = 'siteapp/square.html'


class StonesView(TemplateView):
    template_name = 'siteapp/stones.html'


class GreenHouseView(TemplateView):
    template_name = 'siteapp/greenhouse.html'


class HallView(TemplateView):
    template_name = 'siteapp/hall.html'


class KitchenView(TemplateView):
    template_name = 'siteapp/kitchen.html'


class LoftView(TemplateView):
    template_name = 'siteapp/loft.html'


class FishermanView(TemplateView):
    template_name = 'siteapp/fisherman.html'


class ForgeView(TemplateView):
    template_name = 'siteapp/forge.html'
