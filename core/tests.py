from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import UserProfile

# UserProfile 모델 테스트
class UserProfileModelTest(TestCase):

    def test_create_user_profile(self):
        # 사용자 프로필 생성 테스트
        profile = UserProfile.objects.create(
            username="testuser",
            email="test@example.com",
            bio="테스트 소개"
        )
        self.assertEqual(profile.username, "testuser")
        self.assertEqual(profile.email, "test@example.com")

# UserProfile API 테스트
class UserProfileAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.profile = UserProfile.objects.create(
            username="apitest",
            email="api@example.com",
            bio="API 테스트"
        )

    def test_get_profiles(self):
        # 프로필 목록 API 테스트
        response = self.client.get(reverse("userprofile-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["username"], "apitest")
