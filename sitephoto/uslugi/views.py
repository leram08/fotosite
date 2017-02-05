from django.shortcuts import render
from .models import*

def show_uslugi(request):
    #import pdb; pdb.set_trace()
    photos_uslugi = uslugi_photo.objects.all()
    videos_uslugi = uslugi_video.objects.all()
    #import pdb; pdb.set_trace()
    context={
        "photos_uslugi":photos_uslugi,
        "videos_uslugi":videos_uslugi,
        }
    #import pdb; pdb.set_trace()
    return render(request, 'uslugi.html', context)