"""This file tests explore/views.py"""

import pytest
from django.urls import reverse
from library.models import Destination


@pytest.fixture
def logged_in_client(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="test", password="pass")
    client.login(username="test", password="pass")
    return client, user


def test_world_map_redirect_if_not_logged_in(client):
    response = client.get(reverse('explore:world_map'))

    # Check for correct redirection
    assert response.status_code == 302  # Default redirect status code
    assert response.url.startswith('/accounts/login/')


def test_render_world_map(logged_in_client):
    client, user = logged_in_client
    response = client.get(reverse('explore:world_map'))

    # Check HTTP status
    assert response.status_code == 200

    # Check for correct template
    templates = [t.name for t in response.templates if t.name is not None]
    assert 'explore/world_map.html' in templates

    # Check for forms
    assert 'country_form' in response.context
    assert 'city_form' in response.context


@pytest.mark.django_db
def test_coord_retrieval_from_Destination_model(logged_in_client):
    client, user = logged_in_client
    
    # Create entry in Destination model
    Destination.objects.create(
        owner=user,
        latitude=10.0,
        longitude=20.0,
    )
    response = client.get(reverse('explore:world_map'))

    # Check for correct coord retrieval
    assert len(response.context["destinations"]) == 1
    assert response.context["destinations"][0]["latitude"] == 10.0
    assert response.context["destinations"][0]["longitude"] == 20.0
