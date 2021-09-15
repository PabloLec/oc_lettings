import pytest
from django.urls import reverse
from lettings.models import Letting, Address

pytestmark = pytest.mark.django_db


class TestAddress:
    def test_creation(self):
        assert Address.objects.get(street="Rue de la Paix")

    def test_update(self):
        address = Address.objects.get(street="Rue de la Paix")
        address.zip_code = "75001"
        address.save()
        with pytest.raises(Address.DoesNotExist):
            assert Address.objects.get(zip_code="75000")
        assert Address.objects.get(zip_code="75001")

    def test_deletion(self):
        address = Address.objects.get(street="Rue de la Paix")
        address.delete()
        with pytest.raises(Address.DoesNotExist):
            assert Address.objects.get(street="Rue de la Paix")


class TestLetting:
    def test_creation(self):
        assert Letting.objects.get(title="Dummy Letting")

    def test_update(self):
        letting = Letting.objects.get(title="Dummy Letting")
        letting.title = "Changed title"
        letting.save()
        with pytest.raises(Letting.DoesNotExist):
            assert Letting.objects.get(title="Dummy Letting")
        assert Letting.objects.get(title="Changed title")

    def test_deletion(self):
        letting = Letting.objects.get(title="Dummy Letting")
        letting.delete()
        with pytest.raises(Letting.DoesNotExist):
            assert Letting.objects.get(title="Dummy Letting")


def test_index(client):
    response = str(client.get(reverse("lettings:index")).content)
    assert "<title>Lettings</title>" in response
    lettings = Letting.objects.all()
    for el in lettings:
        assert el.title in response


def test_letting_page(client):
    lettings = Letting.objects.all()
    for el in lettings:
        response = str(client.get(reverse("lettings:letting", args=(el.pk,))).content)
        assert el.title in response
        assert str(el.address.number) in response and el.address.street in response
