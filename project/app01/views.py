from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from models import UserInfo
from serializer import UserInfoSerializer
from filter import UserInfoFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    filter_class = UserInfoFilter
    filter_fields = ['username', ]
    search_fields = ('username',)
