from django import forms
from django.contrib.auth.models import User
from .models import Resource, Course

class UploadForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.order_by('name')

    class Meta:
        model = Resource
        # major hier tussen zetten wanneer filteren werkt
        fields = ('title', 'course', 'resourcetype', 'resourcefile')


class AddCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('name', 'course_id', 'major')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
