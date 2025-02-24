from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Media
from .forms import MediaUploadForm

def home(request):
    """Home page displaying uploaded media."""
    media_files = Media.objects.all()
    return render(request, 'home.html', {'media_files': media_files})

def upload_media(request):
    """Handles media uploads."""
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MediaUploadForm()
    return render(request, 'upload.html', {'form': form})

def media_detail(request, media_id):
    """Display details of a single media file."""
    media = Media.objects.get(id=media_id)
    print(media.file.url)
    return render(request, 'media_detail.html', {'media': media})
