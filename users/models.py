from django.db import models

class CustomUserModel(models.Model):
    user_id = models.UUIDField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
