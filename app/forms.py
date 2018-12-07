from django.forms import Form
from django import forms


class CreateForm(Form):
    name = forms.CharField(label="Name")
    message = forms.CharField(label="Message")
