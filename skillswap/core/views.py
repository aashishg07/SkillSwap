from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        user = self.request.user
        profile_data = request.data.copy()
        profile_data['user'] = user.id
        serializer = self.get_serializer(data=profile_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SkillListingListCreateView(generics.ListCreateAPIView):
    queryset = SkillListing.objects.all()
    serializer_class = SkillListingSerializer


