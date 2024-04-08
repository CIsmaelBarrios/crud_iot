from .models import Crudiot
from rest_framework import viewsets, permissions
from .serializers import Crudserializers

class CrudIotViewSet(viewsets.ModelViewSet):
    queryset=Crudiot.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= Crudserializers
