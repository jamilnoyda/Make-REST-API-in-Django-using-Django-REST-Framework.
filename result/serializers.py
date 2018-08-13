from rest_framework import serializers
from .models import Marksheet, Standard


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'


class MarksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marksheet
        fields = '__all__'
