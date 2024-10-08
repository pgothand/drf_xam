from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Machine, Axis
from .serializers import UserSerializer, MachineSerializer, AxisSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [IsAuthenticated]

class AxisViewSet(viewsets.ModelViewSet):
    queryset = Axis.objects.all()
    serializer_class = AxisSerializer
    permission_classes = [IsAuthenticated]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserSerializer