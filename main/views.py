from django.shortcuts import render, get_object_or_404
from .models import Resource, Course
from .forms import UploadForm, AddCourseForm
from django.utils import timezone
from django.shortcuts import redirect
import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def index(request):
    resources = Resource.objects.all()
    return render(request, 'main/index.html', {'resources': resources})

def about(request):
    return render(request, 'main/about.html')

def courses(request):
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
    course = get_object_or_404(Course, pk=pk)
    resources = Resource.objects.filter(course__name = course)
    return render(request, 'main/course.html', {'course': course, 'resources': resources})

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            resourceupload = form.save(commit=False)
            resourceupload.uploadedBy = request.user
            resourceupload.upload_date = timezone.now()
            resourceupload.save()
            return redirect('course', pk=resourceupload.course.pk)
    else:
        form = UploadForm()
    return render(request, 'main/upload.html', {'form': form})

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
    query = request.GET['q']
    results = Course.objects.filter(name__contains=query)
    temp = get_template('main/searchresults.html')
    context = Context({'results': results, 'query': query})
    return HttpResponse(temp.render(context))
