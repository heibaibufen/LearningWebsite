from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app01 import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API平台",
        default_version="v1",
        description="接口文档",
        terms_of_service="",
        contact=openapi.Contact(email='769470064@qq.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True
)

router = DefaultRouter()
router.register('UserInfo', UserInfoViewSet, basename='UserInfo')

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
    path('login/', views.login),
    path('register/', views.register),
]
