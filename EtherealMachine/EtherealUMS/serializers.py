from rest_framework import serializers
from .models import CustomUser, Machine, Axis

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'role', 'email']

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class AxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Axis
        fields = '__all__'
