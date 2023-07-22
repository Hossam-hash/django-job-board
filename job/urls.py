from . import views
from django.urls import include, path

app_name='job'


urlpatterns = [

    path('',views.job_list),#all jobs
    path('<str:slug>',views.job_details,name='job_detail'),#one job
]
