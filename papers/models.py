from django.conf import settings
from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    abstract = models.TextField()
    published_at = models.DateField()
    arxiv_url = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]
