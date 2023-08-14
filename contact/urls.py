from . import views
from django.urls import include, path

app_name='contact'


urlpatterns = [

    path('',views.send_message,name='contact'),#all jobs
]