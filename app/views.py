from django.shortcuts import render
from django.views import View
from . import models
from . import forms

# Create your views here.


class GetHome(View):
    def get(self, request):
        guest = models.Guest.objects.all()
        return render(request, 'index.html', {'notes': guest})


class Create(View):
    def get(self, request):
        return render(request, 'create.html',
                      {'create_form': forms.CreateForm()})
