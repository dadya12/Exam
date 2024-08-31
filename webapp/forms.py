from webapp.models import Picture, Album
from django import forms


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['picture', 'caption', 'album', 'private']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'description', 'private']
