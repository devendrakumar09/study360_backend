from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
# Create your views here.
from .models import *
from .serializer import * 

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def hello_world(request):
    response = {'status':200,"message": "Hello, world!"}
    return Response(response)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def categoriesAPI(request):
    response = {'status':200}
    categories_objs = Categories.objects.all() 
    serializer = CategorySerializer(categories_objs, many = True)
    response['data'] = serializer.data
    return Response(response)