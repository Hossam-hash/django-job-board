from django import forms

from .models import Apply

class ApplyForm(forms.ModelForm):#هعمل فورم لموديل موجوده عندى فى الhtml
    class Meta:
        model = Apply
        fields=['name',"email","website",'cv','cover_letter']