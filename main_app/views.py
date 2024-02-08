
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import generics, status, permissions
from .serializers import FlowerSerializer, HydrateSerializer, CustomerSerializer, userSerializer
from .models import Flower, Hydrate, Customer, User
from rest_framework.exceptions import PermissionDenied


# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = userSerializer
    queryset = User.objects.all()
    def create(self, request, *args, **kwargs):
        response = super().create(request,*args,**kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        print(response)
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
            'user':response.data
        })

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh':str(refresh),
                'access':str(refresh.access_token),
                'user': userSerializer(user).data
            })
        return Response({'error': 'Invalid Credentials'}, status = status.HTTP_401_UNAUTHORIZED)
    
class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(username=request.user)
        refresh = RefreshToken.for_user(request.user)
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
            'user': userSerializer(user).data
        })
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
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Flower.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FlowerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user=self.request.user
        return Flower.objects.filter(user=user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        customers_associated = Customer.objects.filter(id__in=instance.customers.all())
        customers_serializer = CustomerSerializer(customers_associated, many=True)
        return Response({
            'flower': serializer.data,
            'customers_associated': customers_serializer.data
    
        })

    def perform_update(self, serializer):
        flower = self.get_object()
        if flower.user != self.request.user:
            raise PermissionDenied({'message':'You do not have permission to edit this flwoer.'})
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied({'message':'You do not have permission to delete this flower.'})

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







