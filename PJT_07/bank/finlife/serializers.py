from .models import DepositProducts, DepositOptions
from rest_framework import serializers

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields='__all__'

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields='__all__'