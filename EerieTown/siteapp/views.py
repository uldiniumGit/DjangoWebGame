from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, View
from .models import PatchNote, GameUser
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm
from django.http import HttpResponse, HttpResponseRedirect


class ChangeKeyView(View):
    def get(self, request):
        user = request.user
        setattr(user, 'has_castle_key', True)
        user.save()
        return redirect('siteapp:index')


class UserCreateView(CreateView):
    model = GameUser
    template_name = 'siteapp/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('siteapp:login')


class UserLoginView(LoginView):
    template_name = 'siteapp/login.html'


class MainView(TemplateView):
    template_name = 'siteapp/index.html'


class PatchesListView(ListView):
    model = PatchNote
    template_name = 'siteapp/patch_list.html'

    def get_queryset(self):
        return super(PatchesListView, self).get_queryset().order_by('-id')
