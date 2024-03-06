from rest_framework.serializers import Serializer
from ..models import PessoaBancoDeDados

class PessoSerializer(modelSerializer): 
    class Meta:
        model = PessoaBancoDeDados
        fields = ['id']