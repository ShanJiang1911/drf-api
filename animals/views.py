from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Animal
from .serializers import AnimalSerializer

class AnimalList(ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer 

class AnimalDetail(RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer 

