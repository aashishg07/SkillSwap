from rest_framework import serializers
from .models import Skill, Profile, SkillListing, SkillExchange, ForumTopic, ForumComment, UserProgress, Notification, Message, MeetingProposal

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class SkillListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillListing
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class MeetingProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingProposal
        fields = '__all__'

class SkillExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillExchange
        fields = '__all__'

class ForumTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumTopic
        fields = '__all__'

class ForumCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumComment
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = '__all__'