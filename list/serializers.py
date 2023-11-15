from rest_framework import serializers
from .models import Startup

class StartupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Startup
        fields = ('id', 'name', 'tagline', 'summary', 'location', 'niche_score', 'website_url', 'linkedin_url', 'created_at', 'fire_score', 'snooze_score')