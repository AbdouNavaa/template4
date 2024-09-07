from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Developper
        fields = '__all__'
        exclude = ['work','slug']
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email'] 
        
class DevForm(forms.ModelForm):
    class Meta:
        model = Developper
        fields = '__all__'
        exclude = ['slug']
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'  
        widgets = {
            'end': forms.DateInput(attrs={'type': 'date'}),
        }
        exclude = ['slug']
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'  
        exclude = ['teacher','slug']
        
class SkillForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'
        exclude = ['dev','slug']
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        exclude = ['creater','slug']
        
class FreindForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['friends']  # Ensure you're only selecting friends

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FreindForm, self).__init__(*args, **kwargs)
        
        if user:
            self.fields['friends'].queryset = Developper.objects.exclude(id=user.id)

    
        
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            
        }
        exclude = ['user','slug']