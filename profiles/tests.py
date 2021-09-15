import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

pytestmark = pytest.mark.django_db


class TestProfile:
    def test_creation(self):
        assert Profile.objects.get(favorite_city="Paris")

    def test_update(self):
        profile = Profile.objects.get(favorite_city="Paris")
        profile.favorite_city = "Berlin"
        profile.save()
        with pytest.raises(Profile.DoesNotExist):
            assert Profile.objects.get(favorite_city="Paris")
        assert Profile.objects.get(favorite_city="Berlin")

    def test_deletion(self):
        profile = Profile.objects.get(favorite_city="Paris")
        profile.delete()
        with pytest.raises(Profile.DoesNotExist):
            assert Profile.objects.get(favorite_city="Paris")


def test_index(client):
    response = str(client.get(reverse("profiles:index")).content)
    assert "<title>Profiles</title>" in response
    profiles = Profile.objects.all()
    for el in profiles:
        assert el.user.username in response


def test_profile_page(client):
    users = User.objects.all()
    for el in users:
        response = str(client.get(reverse("profiles:profile", args=(el.username,))).content)
        assert el.username in response
