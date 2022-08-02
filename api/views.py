from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.urls import reverse
from .apps import ApiConfig 
from rest_framework.permissions import IsAuthenticated
def add_name_scope(view_name: str):
    return ApiConfig.name + ":" + view_name

class HelloView(APIView):
    name = 'hello'

    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get (self, request, *args, **kwargs):
        __view_names = (
                HelloView.name,
                )

        return Response(
                data = {
                    key: request.build_absolute_uri(reverse(add_name_scope(value)))
                    for key, value in zip(__view_names, __view_names)
            },)
