from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from app01.models import UserInfo
from app01.serializer import UserInfoSerializer
from app01.filter import UserInfoFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .models import UserInfo


# Create your views here.


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    filter_class = UserInfoFilter
    filter_fields = ['username', ]
    search_fields = ('username',)


def login(request):
    if request.method == "GET":
        return render(request, "login.html")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    UserInfo.objects.create(username=user, password=pwd)
    return redirect("http://127.0.0.1:8000/api/login/")
