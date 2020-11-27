from django.db import models
from ckeditor.fields import RichTextField
from django.db import models
from paranoid_model.models import Paranoid


class PersonalInformation(Paranoid):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    address = models.TextField(max_length=50)
    city = models.CharField(max_length=50, null=True)
    pin_code = models.CharField(max_length=6)
    email_address = models.CharField(max_length=25, null=True)
    contact_number = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name


class Experience(Paranoid):
    company = models.CharField(max_length=50, null=True)
    job_title = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = RichTextField(max_length=50, null=True)

    def __str__(self):
        return self.company


class Education(Paranoid):
    college_name = models.TextField(max_length=50, null=True)
    university_name = models.TextField(max_length=50, null=True)
    course = models.CharField(max_length=50, null=True)
    grade_cgpa = models.CharField(max_length=5, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    State = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.college_name


LEVEL = (
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Expert', 'Expert')
)


class Skill(Paranoid):
    skill = models.CharField(max_length=50, null=True)
    level = models.CharField(max_length=30, choices=LEVEL, null=True)

    def __str__(self):
        return self.skill


class Achivement(Paranoid):
    achivement = RichTextField(max_length=50)

    def __str__(self):
        return self.achivement


class Report(Paranoid):
    photo = models.CharField(max_length=10, null=True, blank=True)
    personal_information = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE)
    experiance = models.ForeignKey(Experience, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    achivement = models.ForeignKey(Achivement, on_delete=models.CASCADE)

    def __str__(self):
        return self.achivement


# Create your models here.
