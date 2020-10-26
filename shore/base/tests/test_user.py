import pytest
from model_bakery import baker
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED

from shore.base.serializers import UserSerializer

from shore.base.models import User


@pytest.fixture
def user(db):
    return baker.prepare(User)


@pytest.fixture
def resp_user(client, user):
    user_obj = UserSerializer(user).data
    user_obj["password"] = "xpto42"
    return client.post(reverse("clients"), user_obj)


def test_list_users(resp_user):
    assert resp_user.status_code == HTTP_201_CREATED
