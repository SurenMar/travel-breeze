"""This file tests explore/views.py"""

import pytest
from django.urls import reverse
from explore import views

@pytest.fixture
def logged_in_client(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="test", password="pass")
    client.login(username="test", password="pass")
    return client, user

@pytest.mark.django_db
def test_render_world_map(logged_in_client):
    client, user = logged_in_client
    response = client.get('/explore/')

    # Check HTTP status
    assert response.status_code == 200

    # Check for correct template
    templates = [t.name for t in response.templates if t.name is not None]
    assert 'explore/world_map.html' in templates

def test_world_map_redirect_if_not_logged_in(client):
    url = reverse('explore:world_map')
    response = client.get(url)

    assert response.status_code == 302  # Default redirect status code
    assert response.url.startswith('/accounts/login/')
