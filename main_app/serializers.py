from rest_framework import serializers
from .models import Flower, Hydrate

class FlowerSerializer(serializers.ModelSerializer):
    hydrate_for_today = serializers.SerializerMethodField()

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