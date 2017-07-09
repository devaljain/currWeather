from . import views
from django.conf.urls import url

app_name='weather'

urlpatterns = [

    url(r'^$',views.index),
    #/weather/find/
    url(r'^find/',views.find,name='find')
]