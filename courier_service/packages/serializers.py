from rest_framework import serializers
from .models import Package


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
        read_only_fields = ('sender', 'tracking_number', 'created_at', 'updated_at', 'deleted_at')

class PackageSoftDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id']

class PackageLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['sender','description', 'recipient_name', 'status']
