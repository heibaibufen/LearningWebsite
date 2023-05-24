from django.contrib import admin

# Register your models here.
from app01.models import UserInfo

admin.site.site_header = '任务管理系统'


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password',)
    list_display_links = ('username',)
    list_per_page = 50


admin.site.register(UserInfo, UserInfoAdmin)
