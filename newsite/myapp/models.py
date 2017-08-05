from django.db import models

class MessageBoard(models.Model):
    new_message = models.TextField(null=False)