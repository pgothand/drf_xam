# user_management/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MachineViewSet, AxisViewSet, CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'machines', MachineViewSet)
router.register(r'axes', AxisViewSet)

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
]
