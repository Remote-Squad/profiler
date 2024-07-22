from rest_framework import serializers
from .models import Research


class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = ('id', 'query', 'data', 'date_added', 'date_modified')
