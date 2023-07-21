from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Profile


class ProfileViewsTest(TestCase):

    def setUp(self) -> None:
        "Create test user"
        self.user = User.objects.create_user(
            username="lettings-test-User",
            password="user_pass",
            email="test-User@email.com"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city='Brisbane')

    def test_profiles_index(self):
        "Test if profile index url is valid"
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, "<title>Profiles</title>")

    def test_profiles_infos_page(self):
        "Test profile main page url is valid"
        url = reverse('profiles:profile', args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, f"<title>{self.user.username}</title>")
