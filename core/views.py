# Create your views here.
from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer

# UserProfile API ViewSet
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
from django.shortcuts import render

# Create your views here.
