from rest_framework import serializers
from webapp.models import Picture


class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['id', 'author', 'favorite']
        read_only_fields = ('id', 'author')
