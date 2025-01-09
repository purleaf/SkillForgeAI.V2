from django.db import models

class ListeningQuestion(models.Model):
    audio_file = models.FileField(upload_to='listening_audio/')
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=100)
