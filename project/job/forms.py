from django import forms
from .models import Apply, Job, Category

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'cover_letter', 'cv']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug','owner')

class CategoryForm(forms.ModelForm):
    class Meta:
        model =  Category
        fields = '__all__'
