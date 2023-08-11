from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PatchNote
# Create your views here.


def main_view(request):
    return render(request, 'siteapp/index.html', context={})


def patchnotes(request):
    patchnotes = PatchNote.objects.order_by('-id')
    return render(request, 'siteapp/patchnotes.html', context={'patchnotes': patchnotes})
