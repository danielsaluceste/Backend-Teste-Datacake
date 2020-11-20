from rest_framework import viewsets

from .models import todoItem
from .serializers import todoItemSerializer


class todoItemViewSet(viewsets.ModelViewSet):

    serializer_class = todoItemSerializer
    queryset = todoItem.objects.all()