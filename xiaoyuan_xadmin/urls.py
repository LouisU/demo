"""xiaoyuan_xadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
# from students.views_base import StudentsListView  # 演示django自带的view的功能
# from students.views import StudentsListView

########
from students.views import StudentsListViewSet
from users.views import SmsCodeViewset, UserViewSet
# student_list = StudentsListViewSet.as_view({
#     'get': 'list',
# })
########

from rest_framework.routers import DefaultRouter

from rest_framework.documentation import include_docs_urls
# import xadmin
# xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
# from xadmin.plugins import xversion
# xversion.register_models()


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'students', StudentsListViewSet, base_name="students")
router.register(r'register_codes', SmsCodeViewset, base_name="codes")
router.register(r'users', UserViewSet, base_name='users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path(r'xadmin/', include(xadmin.site.urls)),
    # path('students/', student_list),
    path(r'', include(router.urls)),
    path('docs/', include_docs_urls(title='小demo')),

    # drf自带的Token认证， 缺点1. 没有过期机制 2. 需要在服务器和数据库交换才能拿到用户信息。
    # path(r'api-token-auth/', views.obtain_auth_token),

    # jwt的认证过接口
    path(r'login/', obtain_jwt_token),
]
