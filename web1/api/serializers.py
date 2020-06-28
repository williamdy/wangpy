from rest_framework import serializers
from web1.api.models import Product

# type_name = Type.objects.values('type_name').all()
# TYPE_CHOICES = [item['type_name'] for item in type_name]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
