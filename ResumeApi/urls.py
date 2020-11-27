from django.urls import path
from .views import *
urlpatterns = [
    path('personalinformation', PersonalInformationView.as_view()),
    path('personalinformation/<int:id>', PersonalInformationUpdateView.as_view()),

    path('Experience', ExperienceView.as_view()),
    path('Experience/<int:id>', ExperienceUpdateView.as_view()),

    path('Education', EducationView.as_view()),
    path('Education/<int:id>', EducationUpdateView.as_view()),

    path('Skill', SkillView.as_view()),
    path('Skill/<int:id>', SkillUpdateView.as_view()),

    path('Achivement', AchivementView.as_view()),
    path('Achivement/<int:id>', AchivementUpdateView.as_view()),
]