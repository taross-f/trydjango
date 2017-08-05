from django.db import models

class TodoBoard(models.Model):
    new_message = models.CharField(max_length=200,)
    image_url = models.ImageField(upload_to='images/',null=True)
    created_at = models.DateTimeField(auto_now_add=True,)
