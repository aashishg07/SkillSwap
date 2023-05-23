from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=255)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    skills = models.ManyToManyField(Skill)

class SkillListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    skill_offered = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="listing_offered")
    skill_desired = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="listing_desired")




