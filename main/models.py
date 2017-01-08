from django.db import models
from django.utils import timezone



class Course(models.Model):
    name = models.CharField(max_length=70)
    course_id = models.CharField(max_length=10, default="")
    major = models.CharField(
        max_length=45,
        choices= (
        ('bachelorcollege', 'Bachelor College'),
        ('appliedmathematics', 'Applied Mathematics'),
        ('appliedphysics', 'Applied Physics'),
        ('architecture', 'Architecture, Urbanism and Building Sciences'),
        ('automotive', 'Automotive'),
        ('biomedicalengineering', 'Biomedical Engineering'),
        ('chemicalengineering', 'Chemical Engineering'),
        ('computerscience', 'Computer Science'),
        ('electricalengineering', 'Electrical Engineering'),
        ('industrialdesign', 'Industrial Design'),
        ('industrialengineering', 'Industrial Engineering'),
        ('mechanicalengineering', 'Mechanical Engineering'),
        ('psychologyandtechnology', 'Psychology and Technology'),
        ('sustainableinnovation', 'Sustainable Innovation'),
        ),
        default='computerscience',
        )
    def __str__(self):
        return self.name

    def __major__(self):
        return self.major


class Resource(models.Model):
    uploadedBy = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    resourcefile = models.FileField(blank=False, default="")
    major = models.CharField(
        max_length=45,
        choices= (
        ('bachelorcollege', 'Bachelor College'),
        ('appliedmathematics', 'Applied Mathematics'),
        ('appliedphysics', 'Applied Physics'),
        ('architecture', 'Architecture, Urbanism and Building Sciences'),
        ('automotive', 'Automotive'),
        ('biomedicalengineering', 'Biomedical Engineering'),
        ('chemicalengineering', 'Chemical Engineering'),
        ('computerscience', 'Computer Science'),
        ('electricalengineering', 'Electrical Engineering'),
        ('industrialdesign', 'Industrial Design'),
        ('industrialengineering', 'Industrial Engineering'),
        ('mechanicalengineering', 'Mechanical Engineering'),
        ('psychologyandtechnology', 'Psychology and Technology'),
        ('sustainableinnovation', 'Sustainable Innovation'),
        ),
        #default='computerscience',
        )
    #mjr = getattr('Resource', major)
    #courses = models.ForeignKey(Course, on_delete=models.CASCADE, limit_choices_to={'major': mjr})
    course = models.ForeignKey(Course)
    resourcetype = models.CharField(
        max_length=45,
        choices= (
        ('Summary', 'Summary'),
        ('Exam', 'Exam'),
        ),
        default='Summary',
        )
    upload_date = models.DateTimeField(
            blank=True, null=True)
    class Meta:
        ordering = ['course']

    def __str__(self):
        return self.title
