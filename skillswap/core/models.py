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

class SkillExchange(models.Model):
    sender = models.ForeignKey(User, related_name='sent_exchanges', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_exchanges', on_delete=models.CASCADE)
    message = models.TextField()
    meeting_time = models.DateTimeField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)

class ForumTopic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

class ForumComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(ForumTopic, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.topic

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    progress = models.IntegerField()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.sender.username}, To: {self.receiver.username}"

class MeetingProposal(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_proposals')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_proposals')
    meeting_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sender: {self.sender.username}, Receiver: {self.receiver.username}, Meeting Time: {self.meeting_time}"
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.user.username}, Message: {self.message}"