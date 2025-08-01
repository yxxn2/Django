from rest_framework import serializers
from .models import UserProfile

# UserProfile 모델 시리얼라이저
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ["id", "username", "email", "bio", "created_at"]
