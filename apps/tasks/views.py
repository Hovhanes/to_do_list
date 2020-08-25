from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    model = Task
    queryset = Task.objects.all().order_by('-pk')
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_done']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Task.objects.all()
        return Task.objects.filter(user=self.request.user)
