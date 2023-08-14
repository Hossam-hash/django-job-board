from django import forms

from .models import Apply,Job

class ApplyForm(forms.ModelForm):#هعمل فورم لموديل موجوده عندى فى الhtml
    class Meta:
        model = Apply
        fields=['name',"email","website",'cv','cover_letter']


class JobForm(forms.ModelForm):#هعمل فورم لموديل موجوده عندى فى الhtml
    class Meta:
        model = Job
        fields='__all__'
        exclude=('owener','slug')
