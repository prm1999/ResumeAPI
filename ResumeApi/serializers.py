from rest_framework import serializers
from .models import *


class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = [
            'id',
            'first_name',
            'last_name',
            'address',
            'city',
            'pin_code',
            'email_address',
            'contact_number',

        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'id',
            'company',
            'job_title',
            'city',
            'start_date',
            'end_date',
            'description',

        ]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'id',
            'college_name',
            'university_name',
            'course',
            'grade_cgpa',
            'start_date',
            'end_date',
            'State',

        ]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            'id',
            'skill',
            'level',

        ]


class AchivementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achivement
        fields = [
            'id',
            'achivement',
        ]
