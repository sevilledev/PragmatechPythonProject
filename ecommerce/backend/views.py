from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from backend.models import Profile, User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics


class LoginTokenView(TokenObtainPairView):
    serializer_class = TokenPairSerializers


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers


class UserDetail(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = User.objects.filter(id=self.request.user.id)
        serializer = UserSerializers(user, many=True)
        return Response(serializer.data)


class ProfileView(APIView):
    def get(self, request, id):
        profile = Profile.objects.get(user_id=id)
        serializer = ProfileSerializers(profile)
        return Response(serializer.data)

    def put(self, request, id):
        if request.user.is_delivery():
            profile = Profile.objects.get(user_id=id)
            serializer = ProfileSerializers(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def delete(self, request, id):
        profile = Profile.objects.get(user_id=id)
        del profile
        return Response({"success": "Profile deleted!"})
