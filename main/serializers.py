from rest_framework import serializers
from . import models


class HududSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hudud
        fields = '__all__'

class TashkilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tashkilot
        fields = '__all__'

class BinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bino
        fields = '__all__'