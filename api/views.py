from django.shortcuts import get_object_or_404
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import UserSerializer
from users.models import User
#from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status

class UserListAPI(APIView):
    def get(self , request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        
#        renderer = JSONRenderer()
#        users_json = renderer.render(serializer.data)
        
#        return HttpResponse(users_json)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
    class UserDetailAPI(APIView):
        def put(self, request, pk):
            user= get_object_or_404(User, pk=pk)
            serializer = UserSerializer(instance=user,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors) 