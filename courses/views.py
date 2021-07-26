from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from courses.models import Course, HomeworkTask
from courses.permissions import IsAuthOrReadOnly
from courses.serializers import CourseSerializer

print(HomeworkTask.objects.last().solutions.all())


class CoursesView(ListView):
    template_name = 'courses/courses.html'
    queryset = Course.objects.all().prefetch_related(
        'tasks',
        'tasks__solutions',
        'tasks__solutions__user',
    )[:100]


class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CourseSerializer
        else:
            return CourseSerializer

