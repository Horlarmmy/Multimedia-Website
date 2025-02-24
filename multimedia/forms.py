from django import forms
from .models import Media

class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['title', 'description', 'media_type', 'file']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'media_type': 'Media Type',
            'file': 'File',
        }