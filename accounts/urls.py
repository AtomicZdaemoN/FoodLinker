from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CreateUserViewSet, ProviderViewSet, CharityViewSet, MyTokenObtainPairView, UserViewSet

# Set up the router to automatically handle ViewSet URLs
router = DefaultRouter()
router.register(r'provider', ProviderViewSet, basename='provider')
router.register(r'charity', CharityViewSet, basename='charity')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('create-user/', CreateUserViewSet.as_view(), name='create-user'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('account', include(router.urls)),
]
