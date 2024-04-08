from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

from .models import CrudIot
from .serializers import CrudIotSerializer

class CrudIotViewSet(viewsets.ModelViewSet):
    queryset = CrudIot.objects.all()
    serializer_class = CrudIotSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Guarda los datos
            serializer.save()
            
            # Envía el correo electrónico con los datos recibidos
            data = serializer.validated_data
            enviar_correo_electronico(data)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def enviar_correo_electronico(data):
    subject = 'Nuevo mensaje desde tu aplicación'
    message = f'''
    Nombre: {data.get('nombre')}
    Correo: {data.get('correo')}
    Mensaje: {data.get('mensaje')}
    Teléfono: {data.get('telefono')}
    '''
    from_email = 'pao2604diaz@gmail.com'  # Cambia esto por tu dirección de correo electrónico
    to_email = ['claudiobarrios2510@gmail.com']  # Dirección de correo electrónico destino

    send_mail(subject, message, from_email, to_email)
