from rest_framework import serializers
from .models import Flower, Hydrate, Customer
from django.contrib.auth.models import User

class userSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class SimpleFlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    flowers = SimpleFlowerSerializer(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'name', 'flowers']

class SimpleCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class FlowerSerializer(serializers.ModelSerializer):
    customers = SimpleCustomerSerializer(many=True, read_only=True)
    hydrate_for_today = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Flower
        fields = '__all__'

    def get_hydrate_for_today(self,obj):
        return obj.hydrate_for_today()
    
class HydrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hydrate
        fields = '__all__'
        read_only_fields = ('flower',)



