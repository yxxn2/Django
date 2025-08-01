from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet
from .frontend_views import home

# UserProfile API 라우터
router = DefaultRouter()
router.register(r"profiles", UserProfileViewSet)

urlpatterns = [
    path("", home, name="home"),
    path("api/", include(router.urls)),
]
