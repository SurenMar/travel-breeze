import pytest
from django.urls import reverse
from library.models import Destination

@pytest.fixture
def logged_in_client(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="test", password="pass")
    client.login(username="test", password="pass")
    return client, user


def test_destination_list_when_logged_in(logged_in_client):
    client, user = logged_in_client

    response = client.get(reverse('library:destination_list'))

    # Check if page is reached
    assert response.status_code == 200
    assert response.context['title'] == 'Library'
    
    # Check for correct template
    templates = [t.name for t in response.templates if t.name is not None]
    assert 'library/destination_list.html' in templates


@pytest.mark.django_db
def test_correct_detination_list_retrieval(logged_in_client):
    client, user = logged_in_client

    # Create destination entry for current user
    dest = Destination.objects.create(
        owner=user,
        country='country',
        city='city',
    )

    # Create destination entry for other user
    other_dest = Destination.objects.create(
        owner=user.__class__.objects.create_user(
            username="other", password="pass"
        ),
        country='country',
        city='city',
    )

    response = client.get(reverse('library:destination_list'))

    # Check for correct returned destinations
    dests = response.context["destinations"]
    assert dest in dests
    assert other_dest not in dests

def test_destination_list_when_not_logged_in(client):
    response = client.get(reverse('library:destination_list'))

    # Check for correct redirection
    assert response.status_code == 302  # Default redirect status code
    assert response.url.startswith('/accounts/login/')
