from rest_framework import serializers
from .models import Crudiot

class Crudserializers(serializers.ModelSerializer):
            class Meta():
                    model=Crudiot
                    fields=('id','nombre', 'correo', 'mensaje', 'telefono')