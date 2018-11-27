from django.db import models

# Create your models here.
class Conversation(models.Model):
    chatbot = models.ForeignKey('Chatbot', on_delete=models.CASCADE)
    
class ChatbotSetting(models.Model):
    
    
class Entry(models.Model):
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE)
    text = models.TextField()
    ischatbot = models.BooleanField()