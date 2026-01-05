from django.db import models
from django.contrib.auth.models import User

class Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="vault_passwords")
    website = models.URLField()
    username = models.CharField(max_length=100)
    password = models.TextField()
    notes = models.TextField(blank=True)


    def __str__(self):
        return self.website
