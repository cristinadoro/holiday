from django.forms import ModelForm
from django import forms
from models import Person,Planner


class PersonForm(ModelForm):
    class Meta:
        model = Person


class PlannerForm(ModelForm):
    class Meta:
        model = Planner