from rest_framework import serializers
from .models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "keeper", "food", "created_at")
        model = Animal