from django.contrib.auth.models import User, Group
from rest_framework import serializers

from SampleApp.models import Course


class UserSerializer(serializers.ModelSerializer):
    def validate_first_name(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError("First name must contain 'Django'")
        return value

    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ListUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'groups']

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['groups'] = GroupSerializer(instance.groups.all(), many=True).data
        return result
