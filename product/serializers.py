from rest_framework import serializers
from product.models import Product, subscription

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'active', 'introductiondate', 'created_at', 'updated_at')

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscription
        fields = ('product', 'user', 'start_date', 'end_date')