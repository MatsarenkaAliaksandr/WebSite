from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title","task","body"]
        widgets = {"title":TextInput(attrs={'class':'form-control','placeholder':'Inter name'}),
                   "task":Textarea(attrs={'class':'form-control','placeholder':'Inter name'}),
                   "body":Textarea(attrs={'class':'form-control','placeholder':'Inter body'}),}
