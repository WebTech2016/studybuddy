from django import forms
from django.contrib.auth.models import User
from .models import Resource, Course

class UploadForm(forms.ModelForm):

    class Meta:
        model = Resource
        fields = ('title', 'major', 'course', 'resourcetype', 'resourcefile')


class AddCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('name', 'course_id', 'major')
