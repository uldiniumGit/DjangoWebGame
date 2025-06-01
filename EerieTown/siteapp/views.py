from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import GameUser
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm, LoginForm


# Универсальный класс для установки булевого флага пользователя и редиректа
class SetUserFlagView(LoginRequiredMixin, View):
    flag_name = None  # Имя поля у пользователя
    flag_value = True
    redirect_url = 'siteapp:index'

    def get(self, request):
        if not self.flag_name:
            return redirect(self.redirect_url)
        setattr(request.user, self.flag_name, self.flag_value)
        request.user.save()
        return redirect(self.redirect_url)


# Ключи
class GetMasterKeyView(LoginRequiredMixin, View):
    def get(self, request):
        keys = [
            'has_forge_key',
            'has_greenhouse_key',
            'has_stones_key',
            'has_loft_key',
            'has_kitchen_key',
            'has_fisherman_key'
        ]
        for key in keys:
            setattr(request.user, key, True)
        request.user.save()
        return redirect('siteapp:index')


class LoseMasterKeyView(LoginRequiredMixin, View):
    def get(self, request):
        keys_to_reset = [
            'has_forge_key',
            'has_greenhouse_key',
            'has_stones_key',
            'has_loft_key',
            'has_kitchen_key',
            'has_fisherman_key',
            'day_two',
            'day_three',
            'end'
        ]
        for key in keys_to_reset:
            setattr(request.user, key, False)
        request.user.save()
        return redirect('siteapp:index')


class GetForgeKeyView(SetUserFlagView):
    flag_name = 'has_forge_key'


class GetGreenhouseKeyView(SetUserFlagView):
    flag_name = 'has_greenhouse_key'


class GetStonesKeyView(SetUserFlagView):
    flag_name = 'has_stones_key'
    redirect_url = 'siteapp:fisherman'


class GetLoftKeyView(SetUserFlagView):
    flag_name = 'has_loft_key'
    redirect_url = 'siteapp:hall'


class GetKitchenKeyView(SetUserFlagView):
    flag_name = 'has_kitchen_key'


class GetFishermanKeyView(SetUserFlagView):
    flag_name = 'has_fisherman_key'


# Смена дня
class DayTwoView(SetUserFlagView):
    flag_name = 'day_two'
    redirect_url = 'siteapp:loft'


class DayThreeView(SetUserFlagView):
    flag_name = 'day_three'
    redirect_url = 'siteapp:greenhouse'


# Конец
class EndView(SetUserFlagView):
    flag_name = 'end'
    redirect_url = 'siteapp:square'


# Вспомогательные страницы
class UserCreateView(CreateView):
    model = GameUser
    template_name = 'siteapp/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('siteapp:login')


class UserLoginView(LoginView):
    template_name = 'siteapp/login.html'
    authentication_form = LoginForm


class AboutView(TemplateView):
    template_name = 'siteapp/patch_list.html'


class HelpView(TemplateView):
    template_name = 'siteapp/help.html'


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
