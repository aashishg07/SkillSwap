from django.urls import path
from .views import UserListCreateView, SkillListCreateView, ProfileListCreateView, SkillListingListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('skills/', SkillListCreateView.as_view(), name='skill-list'),
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list'),
    path('skill-listings/', SkillListingListCreateView.as_view(), name='skill-listing-list'),
]