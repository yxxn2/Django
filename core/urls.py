from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet

# UserProfile API 라우터
router = DefaultRouter()
router.register(r"profiles", UserProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
