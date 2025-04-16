"""
Blank URLConf just to keep the test suite happy
"""
from django.urls import re_path
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_jwt import views
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class MockView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        return HttpResponse({'a': 1, 'b': 2, 'c': 3})

urlpatterns = [
    re_path(r'^auth-token/$', views.obtain_jwt_token),
    re_path(r'^auth-token-refresh/$', views.refresh_jwt_token),
    re_path(r'^auth-token-verify/$', views.verify_jwt_token),
    re_path(r'^jwt/$', MockView.as_view(
        authentication_classes=[JSONWebTokenAuthentication])),
]
