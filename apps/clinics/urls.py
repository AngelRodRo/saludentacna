from django.conf.urls import patterns,  url

from .views import ClinicList, ClinicSearch

urlpatterns = patterns('',

    # url(r'^$', clinicindex.as_view(),name='index'),
    # url(r'^add/$', RegisterClinic.as_view(),name='clinic_add'),
    url(r'^$', ClinicList.as_view(),name='clinic_list'),
    url(r'^search/$', ClinicSearch.as_view(),name='clinic_search')
    # url(r'^(?P<pk>\d+)/$', ClinicaDetailView.as_view(),name='clinic_detail'),
)