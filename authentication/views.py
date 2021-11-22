from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import ChangePasswordSerializer, UserSerializer,LoginSerializer

from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import jwt
from django.contrib import auth
# Create your views here.
class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    def post(self, request):
        data  = request.data
        username = data.get('username','')
        oldpassword = data.get('oldpassword','') 
        user = auth.authenticate(username=username,password=oldpassword)
        if user:
            serializer = ChangePasswordSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail' :'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        data  = request.data
        username = data.get('username','')
        password = data.get('password','') 
        user = auth.authenticate(username=username,password=password)

        if user:
            
            auth_token = jwt.encode({'username':user.username},settings.JWT_SECRET_KEY)
            
            data = {"token": auth_token}
            
            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail' :'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


    