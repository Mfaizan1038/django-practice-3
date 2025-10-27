from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Post(models.Model):
    title = models.CharField(max_length=100)

class Photo(models.Model):
    caption = models.CharField(max_length=100)


class Comment(models.Model):
    text = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Comment on {self.content_object}: {self.text[:20]}"

