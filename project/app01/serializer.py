from app01.models import UserInfo
from rest_framework import serializers


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
