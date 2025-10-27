from django.db import models

class TopStudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(marks__gte=90)