from django.shortcuts import render, get_object_or_404
from .models import Resource, Course
from .forms import UploadForm, AddCourseForm, UserForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = UserForm()
    resources = Resource.objects.all()
    summaries = Resource.objects.filter(resourcetype = "Summary")
    exams = Resource.objects.filter(resourcetype = "Exam")
    courses = Course.objects.all()
    return render(request, 'main/index.html', {'resources': resources, 'summaries': summaries, 'exams': exams, 'courses': courses, 'form': form})

def about(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('about')
    else:
        form = UserForm()
    return render(request, 'main/about.html')

def courses(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('courses')
    else:
        form = UserForm()

    courses = Course.objects.all()
    bachelorcollege = Course.objects.filter(major__icontains = "bachelorcollege").order_by("name")
    appliedmathematics = Course.objects.filter(major__icontains = "appliedmathematics").order_by("name")
    appliedphysics = Course.objects.filter(major__icontains = "appliedphysics").order_by("name")
    architecture = Course.objects.filter(major__icontains = "architecture").order_by("name")
    automotive = Course.objects.filter(major__icontains = "automotive").order_by("name")
    biomedicalengineering = Course.objects.filter(major__icontains = "biomedicalengineering").order_by("name")
    chemicalengineering = Course.objects.filter(major__icontains = "chemicalengineering").order_by("name")
    computerscience = Course.objects.filter(major__icontains = "computerscience").order_by("name")
    electricalengineering = Course.objects.filter(major__icontains = "electricalengineering").order_by("name")
    industrialdesign = Course.objects.filter(major__icontains = "industrialdesign").order_by("name")
    industrialengineering = Course.objects.filter(major__icontains = "industrialengineering").order_by("name")
    mechanicalengineering = Course.objects.filter(major__icontains = "mechanicalengineering").order_by("name")
    psychologyandtechnology = Course.objects.filter(major__icontains = "psychologyandtechnology").order_by("name")
    sustainableinnovation = Course.objects.filter(major__icontains = "sustainableinnovation").order_by("name")

    return render(request, 'main/courses.html', {'courses': courses, 'bachelorcollege': bachelorcollege, 'appliedmathematics': appliedmathematics, 'appliedphysics': appliedphysics, 'architecture': architecture,
    'automotive': automotive, 'biomedicalengineering': biomedicalengineering, 'chemicalengineering': chemicalengineering, 'computerscience': computerscience, 'electricalengineering': electricalengineering,
    'industrialdesign': industrialdesign, 'industrialengineering': industrialengineering, 'mechanicalengineering': mechanicalengineering,
    'psychologyandtechnology': psychologyandtechnology, 'sustainableinnovation': sustainableinnovation})

def course(request, pk):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('course', pk=pk)
    else:
        form = UserForm()
    course = get_object_or_404(Course, pk=pk)
    resources = Resource.objects.filter(course__name = course)
    summaries = Resource.objects.filter(course__name = course).filter(resourcetype = "Summary")
    exams = Resource.objects.filter(course__name = course).filter(resourcetype = "Exam")
    return render(request, 'main/course.html', {'course': course, 'resources': resources, 'summaries': summaries, 'exams': exams})

def upload(request):
    formupl = UploadForm()
    form = UserForm()
    if request.method == "POST":
        formupl = UploadForm(request.POST or None, request.FILES or None)
        form = UserForm(request.POST)
        if request.POST.get("form_type") == 'formupload':
            if formupl.is_valid():
                resourceupload = formupl.save(commit=False)
                resourceupload.uploadedBy = request.user
                resourceupload.upload_date = timezone.now()
                resourceupload.save()
                return redirect('course', pk=resourceupload.course.pk)
        elif request.POST.get("form_type") == 'formreg':
            if form.is_valid():
                new_user = User.objects.create_user(**form.cleaned_data)
                login(request, new_user)
                return redirect('upload')
    else:
        formupl = UploadForm()
        form = UserForm()
    return render(request, 'main/upload.html', {'formupl': formupl, 'form': form})

def addcourse(request):
    if request.method == "POST":
        form = AddCourseForm(request.POST or None)
        if form.is_valid():
            courseadd = form.save(commit=False)
            courseadd.save()
            return redirect('upload')
    else:
        form = AddCourseForm()
    return render(request, 'main/addcourse.html', {'form': form})

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404

def search(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = UserForm()

    query = request.GET['q']
    results = Resource.objects.filter(title__contains=query)
    courses = Course.objects.filter(name__contains=query)
    summaries = Resource.objects.filter(title__contains=query).filter(resourcetype = "Summary")
    exams = Resource.objects.filter(title__contains=query).filter(resourcetype = "Exam")
    temp = get_template('main/searchresults.html')
    context = Context({'results': results, 'query': query})
    return render(request, 'main/searchresults.html', {'courses': courses, 'summaries': summaries, 'results': results, 'exams': exams, 'query': query} )
