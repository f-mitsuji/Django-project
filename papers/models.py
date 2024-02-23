from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    abstract = models.TextField()
    published_at = models.DateField()
    arxiv_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title
