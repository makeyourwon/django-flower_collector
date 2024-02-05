
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import FlowerSerializer
from .models import Flower


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