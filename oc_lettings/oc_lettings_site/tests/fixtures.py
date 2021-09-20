import pytest
from django.contrib.auth.models import User
from lettings.models import Letting, Address
from profiles.models import Profile


def create_adresses_and_lettings():
    address1 = Address.objects.create(
        number="10",
        street="Rue de la Paix",
        city="Paris",
        state="FR",
        zip_code="75000",
        country_iso_code="FRA",
    )
    address2 = Address.objects.create(
        number="1600",
        street="Amphitheatre Pkwy",
        city="Mountain View",
        state="CA",
        zip_code="94043",
        country_iso_code="USA",
    )
    address3 = Address.objects.create(
        number="15010",
        street="NE 36th",
        city="Redmond",
        state="WA",
        zip_code="98052",
        country_iso_code="USA",
    )
    Letting.objects.create(title="Dummy Letting", address=address1)
    Letting.objects.create(title="Empty Letting", address=address2)
    Letting.objects.create(title="Vain Letting", address=address3)


def create_users_and_profiles():
    user1 = User.objects.create(username="User1")
    user2 = User.objects.create(username="User2")
    user3 = User.objects.create(username="User3")
    Profile.objects.create(user=user1, favorite_city="Paris")
    Profile.objects.create(user=user2, favorite_city="London")
    Profile.objects.create(user=user3)


@pytest.fixture(scope="session", autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        create_adresses_and_lettings()
        create_users_and_profiles()
