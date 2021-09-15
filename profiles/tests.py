import pytest
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
