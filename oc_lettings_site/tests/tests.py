from django.urls import reverse


def test_index(client):
    expected_elements = ("Holiday Homes", "Profiles", "Lettings")
    response = str(client.get(reverse("index")).content)
    for el in expected_elements:
        assert el in response
