# Create your views here.
from django.db.models import Q
from django.shortcuts import render_to_response
from forms import PersonForm
from forms import PlannerForm
from django.http import HttpResponseRedirect
from django.template import RequestContext



def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_person/thanks/')
    else:
        form = PersonForm()
    return render_to_response('holidays/add_person.html', {'form': form},context_instance=RequestContext(request))


def add_planner(request):
    if request.method == 'POST':
        form = PlannerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = PlannerForm()
    return render_to_response('holidays/add_planner.html', {'form': form},context_instance=RequestContext(request))
