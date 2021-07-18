from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text'] #references attribute 'text' in Topic class in models.py
        labels = {'text': ''} #dictionary

