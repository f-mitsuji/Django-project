from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    abstract = models.TextField()
    publish_date = models.DateField()
    arxiv_id = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.title
