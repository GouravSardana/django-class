from django.shortcuts import render
from django.views.generic import TemplateView,ListView

from home.models import Medical_library


class Hey(ListView):
    template_name = 'hey.html'
    model = Medical_library
    key = Medical_library.objects.all()

