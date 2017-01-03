from django.db import models
from django.utils import timezone


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
        ('sustainableinnovations', 'Sustaibable Innovation'),
        ),
        default='bachelorcollege',
        )
    course = models.CharField(max_length=70, default="")
    resourcetype = models.CharField(
        max_length=45,
        choices= (
        ('summary', 'Summary'),
        ('practiceexam', 'Practice Exam'),
        ('oldexam', 'Old Exam'),
        ),
        default='summary',
        )
    upload_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.title
