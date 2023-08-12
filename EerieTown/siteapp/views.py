from django.views.generic import TemplateView, ListView
from .models import PatchNote
# Create your views here.


class MainView(TemplateView):
    template_name = 'siteapp/index.html'


class PatchesListView(ListView):
    model = PatchNote
    template_name = 'siteapp/patch_list.html'

    def get_queryset(self):
        return super(PatchesListView, self).get_queryset().order_by('-id')
