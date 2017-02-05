from django.shortcuts import render
from .models import *
# Create your views here.

def photo_list(request):
    #import pdb; pdb.set_trace()
    albums = Item.objects.all()
    #import pdb; pdb.set_trace()
    context={
        "albums":albums,
        }
    #import pdb; pdb.set_trace()
    return render(request, 'album.html', context)


def show_photo(request):
    #import pdb; pdb.set_trace()
    photos = Photo.objects.all()
    #import pdb; pdb.set_trace()
    context={
        "photos":photos,
        }
    #import pdb; pdb.set_trace()
    return render(request, 'photo.html', context)

def main(request):
	return render(request, 'main.html')

def uslugi_view(request):
    return render(request, 'uslugi.html')

def slider_main(request):
    slid = Slider.objects.all()
    context={'slid':slid}
    return render(request, 'main.html', context)