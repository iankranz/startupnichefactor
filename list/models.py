from django.db import models
import uuid

class Startup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    summary = models.TextField()
    location = models.CharField(max_length=50)
    niche_score = models.BigIntegerField()
    website_url = models.CharField(max_length=300)
    linkedin_url = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
