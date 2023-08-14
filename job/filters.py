import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):

    class Meta:
        model = Job
        fields = '__all__'
        exclude=['owener','puplished_at','image','salary',"vacancy",'slug']