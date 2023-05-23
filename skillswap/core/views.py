from rest_framework import generics
from .models import Skill, SkillListing, ForumComment, UserProgress, Message, Notification, MeetingProposal, SkillListing, Message, ForumTopic, ForumComment
from .serializers import SkillSerializer, SkillListingSerializer, MessageSerializer, MeetingProposalSerializer, ForumTopicSerializer, ForumCommentSerializer, NotificationSerializer, UserProgressSerializer
from rest_framework.permissions import IsAuthenticated


class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]


class SkillRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]


class SkillListingListCreateView(generics.ListCreateAPIView):
    queryset = SkillListing.objects.all()
    serializer_class = SkillListingSerializer
    permission_classes = [IsAuthenticated]


class SkillListingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SkillListing.objects.all()
    serializer_class = SkillListingSerializer
    permission_classes = [IsAuthenticated]


class ForumTopicListCreateView(generics.ListCreateAPIView):
    queryset = ForumTopic.objects.all()
    serializer_class = ForumTopicSerializer
    permission_classes = [IsAuthenticated]


class ForumTopicRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumTopic.objects.all()
    serializer_class = ForumTopicSerializer
    permission_classes = [IsAuthenticated]


class ForumCommentListCreateView(generics.ListCreateAPIView):
    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentSerializer
    permission_classes = [IsAuthenticated]


class ForumCommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentSerializer
    permission_classes = [IsAuthenticated]


class UserProgressListCreateView(generics.ListCreateAPIView):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer
    permission_classes = [IsAuthenticated]


class UserProgressRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer
    permission_classes = [IsAuthenticated]

class SkillsListCreateAPIView(generics.ListCreateAPIView):
    queryset = SkillListing.objects.all()
    serializer_class = SkillListingSerializer
    permission_classes = [IsAuthenticated]

class SkillListingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SkillListing.objects.all()
    serializer_class = SkillListingSerializer
    permission_classes = [IsAuthenticated]

class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

class MessageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

class MeetingProposalListCreateAPIView(generics.ListCreateAPIView):
    queryset = MeetingProposal.objects.all()
    serializer_class = MeetingProposal
    permission_classes = [IsAuthenticated]

class MeetingProposalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MeetingProposal.objects.all()
    serializer_class = MeetingProposal
    permission_classes = [IsAuthenticated]


class ForumListCreateAPIView(generics.ListCreateAPIView):
    queryset = ForumTopic.objects.all()
    serializer_class = ForumTopicSerializer
    permission_classes = [IsAuthenticated]


class ForumTopicDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumTopic.objects.all()
    serializer_class = ForumTopicSerializer
    permission_classes = [IsAuthenticated]

class ForumCommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentSerializer
    permission_classes = [IsAuthenticated]

class ForumCommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentSerializer
    permission_classes = [IsAuthenticated]

class NotificationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

class NotificationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]