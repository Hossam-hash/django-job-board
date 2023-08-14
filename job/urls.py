from . import views
from django.urls import include, path

app_name='job'


urlpatterns = [

    path('',views.job_list,name='job_list'),#all jobs
    path('add', views.add_job, name='add_job'),  # add job
    path('<str:slug>',views.job_details,name='job_detail'),#one job
]
