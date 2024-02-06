
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import FlowerSerializer, HydrateSerializer
from .models import Flower, Hydrate


# Create your views here.

class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to flower_collector app.'}
        return Response(content)
    

class FlowerList(generics.ListCreateAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

class FlowerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    lookup_field = 'id'

class HydrateList(generics.ListCreateAPIView):
    serializer_class = HydrateSerializer

    def get_queryset(self):
        flower_id = self.kwargs['flower_id']
        return Hydrate.objects.filter(flower_id=flower_id)
    def perform_create(self, serializer):
        flower_id = self.kwargs['flower_id']
        flower = Flower.objects.get(id=flower_id )
        serializer.save(flower=flower)


class HydrateDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HydrateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        flower_id = self.kwargs['flower_id']
        return Hydrate.objects.filter(flower_id=flower_id)
