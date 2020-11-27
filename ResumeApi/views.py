from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class PersonalInformationView(generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = PersonalInformationSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(PersonalInformation.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonalInformationUpdateView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = PersonalInformationSerializer

    def get(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(PersonalInformation, pk=kwargs['id'])
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(PersonalInformation, pk=kwargs['id'])
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(PersonalInformation, pk=kwargs['id'])
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExperienceView(generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = ExperienceSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Experience.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExperienceUpdateView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = ExperienceSerializer

    def get(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Experience, pk=kwargs['id'])
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Experience, pk=kwargs['id'])
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Experience, pk=kwargs['id'])
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EducationView(generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = EducationSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Education.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationUpdateView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = EducationSerializer

    def get(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Education, pk=kwargs['id'])
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Education, pk=kwargs['id'])
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Education, pk=kwargs['id'])
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SkillView(generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = SkillSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Skill.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillUpdateView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = SkillSerializer

    def get(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Skill, pk=kwargs['id'])
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Skill, pk=kwargs['id'])
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Skill, pk=kwargs['id'])
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AchivementView(generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = AchivementSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(Achivement.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AchivementUpdateView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = AchivementSerializer

    def get(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Achivement, pk=kwargs['id'])
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Achivement, pk=kwargs['id'])
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Achivement, pk=kwargs['id'])
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
