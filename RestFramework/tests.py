import math
import logging

from django.contrib.auth.models import Group, User
from pytest_django.fixtures import db

logger = logging.getLogger()

# def test_sqrt():
#     num = 25
#     assert math.sqrt(num) == 5
#
#
# def testsquare():
#     num = 7
#     assert 7 * 7 == 40
#
#
# def tesequality():
#     assert 10 == 11


import pytest

# @pytest.fixture
# def input_value():
#     input = 39
#     return input
#
#
# def test_divisible_by_3(input_value):
#     assert input_value % 3 == 0
#
#
# def test_divisible_by_6(input_value):
#     assert input_value % 6 == 0


import factory
from pytest_factoryboy import register


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


register(UserFactory)


@pytest.fixture
def test_factory_fixture(user_factory):
    user = user_factory.create(username="admin", email="admin@gmail.com")
    assert user.username == "admin"
    assert user.email == "admin@gmail.com"


from faker import Faker

fake = Faker()


@register
class MyUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    email = fake.email()

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.groups.add(group)


def test_fake_new_user(my_user_factory):
    logger.info(my_user_factory.username)
    logger.info(my_user_factory.email)
    assert True


@pytest.fixture
def new_user1(db, my_user_factory, group_factory):
    group = group_factory.create()
    user = my_user_factory.create()
    user.groups.add(group)
    return user


def test_new_user1(new_user1):
    logger.info(new_user1.username)
    logger.info(new_user1.email)
    assert new_user1


@register
class UserGroupRelatedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    email = fake.email()

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.groups.add(group)


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = fake.name()


register(GroupFactory)


def test_user_groups(new_user1, group_factory):
    logger.info(new_user1.groups.all())
    assert new_user1.groups.all()


@pytest.mark.parametrize("username, email, validity", [
    ('admin', 'admin@gmail.com', True),
    ('admin1', 'admin1@gmail.com', True),
    ('admin2', 'admin2@gmail.com', False)
])
def test_user_parameterize(db, user_factory, username, email, validity):
    test = user_factory(username=username, email=email)
    user = User.objects.all().count()
    assert user == validity
