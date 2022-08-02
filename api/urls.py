from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

urlpatterns = [
        path('', views.ApiRoot.as_view(), name='index'),
        path('hello', views.HelloView.as_view(), name='hello'),
        path('obtain-auth-token', obtain_auth_token, name='obtain_auth_token'),
]
