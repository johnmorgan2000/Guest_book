from django.shortcuts import render, redirect
from django.views import View
import datetime
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

    def post(self, request):
        form = forms.CreateForm(data=request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            models.Guest(name=name, message=message, date=date).save()
            return redirect("home")
        else:
            return render(request, 'create.html', {'create_form': form})
