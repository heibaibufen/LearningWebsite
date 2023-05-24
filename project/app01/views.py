from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app01.models import UserInfo
from app01.serializer import UserInfoSerializer
from app01.filter import UserInfoFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    filter_class = UserInfoFilter
    filter_fields = ['username', ]
    search_fields = ('username',)
