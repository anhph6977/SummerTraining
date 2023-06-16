from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import UserSerializer, GroupSerializer, ListUserSerializer
from rest_framework.views import APIView
from django_filters import rest_framework as rest_filters
from rest_framework import filters


class SampleView(APIView):
    def get(self, request):
        return Response({'data': 'this is a message'})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def get_queryset(self):
        queryset = super(UserViewSet, self).get_queryset()
        date_joined_start = self.request.query_params.get('date_joined_start')
        date_joined_end = self.request.query_params.get('date_joined_end')
        if date_joined_start is not None:
            queryset = queryset.filter(date_joined__gt=date_joined_start)
        if date_joined_end is not None:
            queryset = queryset.filter(date_joined_end__lt=date_joined_end)
        return queryset

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['email', 'username']
    search_fields = ['first_name', 'last_name']


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomUserListView(APIView):
    def get(self, request):
        users = User.objects.prefetch_related('groups')
        users_data = ListUserSerializer(users, many=True, context=request).data
        return Response(users_data)
