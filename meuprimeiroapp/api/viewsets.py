from rest_framework.viewsets import ReadOnlyModelViewSet
from ..models import PessoaBancoDeDados

class PessoaViewSet(ModelViewSet):
    queryset = PessoaBancoDeDados