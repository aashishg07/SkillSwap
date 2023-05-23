from django.urls import path
from .views import *

urlpatterns = [
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillRetrieveUpdateDestroyView.as_view(), name='skill-retrieve-update-destroy'),
    path('skill_listings/', SkillListingListCreateView.as_view(), name='skill-listing-list-create'),
    path('skill_listings/<int:pk>/', SkillListingRetrieveUpdateDestroyView.as_view(), name='skill-listing-retrieve-update-destroy'),
    path('forum_topics/', ForumTopicListCreateView.as_view(), name='forum-topic-list-create'),
    path('forum_topics/<int:pk>/', ForumTopicRetrieveUpdateDestroyView.as_view(), name='forum-topic-retrieve-update-destroy'),
    path('forum_comments/', ForumCommentListCreateView.as_view(), name='forum-comment-list-create'),
    path('forum_comments/<int:pk>/', ForumCommentRetrieveUpdateDestroyView.as_view(), name='forum-comment-retrieve-update-destroy'),
    path('user_progress/', UserProgressListCreateView.as_view(), name='user-progress-list-create'),
    path('user_progress/<int:pk>/', UserProgressRetrieveUpdateDestroyView.as_view(), name='user-progress-retrieve-update-destroy'),
    path('message/', MessageListCreateAPIView.as_view(), name='user-progress-list-create'),
    path('message/<int:pk>/', MessageDetailAPIView.as_view(), name='user-progress-retrieve-update-destroy'),
    path('meeting/', MeetingProposalListCreateAPIView.as_view(), name='user-progress-list-create'),
    path('user_progress/<int:pk>/', MeetingProposalDetailAPIView.as_view(), name='user-progress-retrieve-update-destroy'),
    path('forum/', ForumListCreateAPIView.as_view(), name='user-progress-list-create'),
    path('forums/<int:pk>/', ForumTopicDetailAPIView.as_view(), name='user-progress-retrieve-update-destroy'),
    path('forum_comment/', ForumCommentListCreateAPIView.as_view(), name='user-progress-list-create'),
    path('forum_comments/<int:pk>/', ForumCommentDetailAPIView.as_view(), name='user-progress-retrieve-update-destroy'),
    path('notification/', NotificationListCreateAPIView.as_view(), name='user-progress-list-create'),
    path('notifications/<int:pk>/', NotificationDetailAPIView.as_view(), name='user-progress-retrieve-update-destroy'),
]