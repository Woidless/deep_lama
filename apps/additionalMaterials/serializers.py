# additionalMaterials/serializers.py
from rest_framework import serializers
from .models import AdditionalMaterials

class AdditionalMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalMaterials
        fields = ['name', 'type', 'file_link', 'subject']