from django.conf.urls.defaults import *
from views import current_datetime, hours_ahead
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from holidays.models import Person, Planner, Holiday
from django.views.generic import list_detail
import holidays.views


person_info = {
    "queryset" : Person.objects.all().order_by("-name"),
}

planner_info = {
    "queryset" : Planner.objects.all().order_by("-person"),
    #"extra_context" : {"planner_lists" : Planner.objects.filter(destination__in=[1])}
    # "extra_context" : {"planner_lists" : Holiday.objects.filter(destinations__in=[pks])},
    "extra_context" : {"planner_lists" : Planner.objects.all().order_by("person")},
}


urlpatterns = patterns('',
    # Example:
    (r'^time/$',current_datetime),
    (r'^persons/$', list_detail.object_list, person_info),
    (r'^add_person/$','mysite.holidays.views.add_person'),
    (r'^holidayplanner/$', holidays.views.add_planner),
    (r'^planner_info/$', list_detail.object_list, planner_info),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

)
