from django.conf.urls import include, url
# from .views import checkMachineAPI, createMachineAPI, main, test
from .views import *
from django.urls import path

app_name = "API"

urlpatterns = [
    url(r'^$', main, name='main'),
    path('check/machine', checkMachineAPI, name="check_machine"),
    path('create/machine', createMachineAPI, name="create_machine"),
    url(r'^test/$', test, name="test"),
    url(r'^detail/(?P<pk>\d+)/$', detail, name="detail"),
    url(r'^category/$', category, name="category"),        
    url(r'^g_category/$', g_category, name="g_category"),
    url(r'^r_category/$', r_category, name="r_category"),
    url(r'^b_category/$', b_category, name="b_category"),
    url(r'^f_category/$', f_category, name="f_category"),
    url(r'^write/$', write, name="write")
]
