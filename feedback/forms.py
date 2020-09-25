from django import forms
from django.forms import ModelForm

from .models import Feedback

class FeedbackForm(ModelForm):
    
    class Meta:
        model = Feedback
        fields = ['field1', 'field2', 'field3', 'field4', 'name',]

