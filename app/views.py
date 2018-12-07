from django.shortcuts import render
from django.views import View
from . import forms

# Create your views here.


class GetHome(View):
    def get(self, request):
        return render(request, 'index.html')


class Create(View):
    def get(self, request):
        return render(request, 'create.html',
                      {'create_form': forms.CreateForm()})
