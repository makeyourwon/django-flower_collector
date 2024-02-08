
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import FlowerSerializer, HydrateSerializer, CustomerSerializer
from .models import Flower, Hydrate, Customer


# Create your views here.

class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to flower_collector app.'}
        return Response(content)

class AddFlowerToCustomer(APIView):
    def post(self,request, customer_id, flower_id):
        customer = Customer.objects.get(id = customer_id)
        flower = Flower.objects.get(id = flower_id)
        customer.flowers.add(flower)
        return Response({'message':f'{flower.name} added to {customer.name} list.'})

class RemoveFlowerToCustomer(APIView):
    def post(self,request, customer_id, flower_id):
        customer = Customer.objects.get(id = customer_id)
        flower = Flower.objects.get(id = flower_id)
        customer.flowers.remove(flower)
        return Response({'message':f'{flower.name} removed to {customer.name} list.'})

class FlowerList(generics.ListCreateAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

class FlowerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        customers_associated = Customer.objects.filter(id__in=instance.customers.all())
        customers_serializer = CustomerSerializer(customers_associated, many=True)
        return Response({
            'flower': serializer.data,
            'customers_associated': customers_serializer.data
    
        })

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
    
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'







