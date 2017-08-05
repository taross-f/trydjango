from django.db import models

class TodoBoard(models.Model):
    new_message = models.CharField(max_length=200,)
    created_at = models.DateTimeField(auto_now_add=True,)
