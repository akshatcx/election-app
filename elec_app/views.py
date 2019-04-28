from django.shortcuts import render
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from elec_app.models import ElecModel

# Create your views here.
class Home(TemplateView):
    template_name = 'home/index.html.j2'

class HomeJson(BaseDatatableView):
    model = ElecModel 
