from django.db import models


class ToDo(models.Model):
    task = models.TextField(max_length=100)

