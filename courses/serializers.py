from rest_framework import serializers

from courses.models import Course, HomeworkTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkTask
        fields = ['id', 'number', 'task']


class CourseSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'tasks']

    def validate(self, attrs):
        r = self.context['request']
        if r.method == 'GET':
            pass
        return attrs

    def create(self, validated_data):
        t = validated_data.pop('tasks')
        c = super().create(validated_data)

        for data in t:
            HomeworkTask.objects.create(course=c, **data)

        return c
