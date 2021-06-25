from rest_framework import generics
from .serializers import CompSerializer
from .models import Comp

# Create your views here.
class CompList(generics.ListCreateAPIView):
    queryset = Comp.objects.all()
    serializer_class = CompSerializer

class CompDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comp.objects.all()
    serializer_class = CompSerializer