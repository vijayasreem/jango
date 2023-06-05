# models.py

from django.db import models

class GitHubCredentials(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    url = models.URLField()
    repository_name = models.CharField(max_length=100)

class GitHubList(models.Model):
    title = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    url = models.URLField()
    action = models.CharField(max_length=100)