from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user', 'skills']

class SkillListingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    skill_offered = SkillSerializer(read_only=True)
    skill_desired = SkillSerializer(read_only=True)

    class Meta:
        model = SkillListing
        fields = ['user', 'skill_offered', 'skill_desired']