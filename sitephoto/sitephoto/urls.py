"""sitephoto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from galery.views import photo_list, show_photo
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView
from galery.models import Slider, Video
from galery import views as views_slider
from contact import views as views_contact
from comment import views as views_comment
from blogs import views 
from blogs.models import Blogs
from uslugi import views as views_uslugi
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views_slider.slider_main, name="slider_main"),
    url(r'^uslugi/', views_uslugi.show_uslugi, name='show_uslugi'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^blog/', views.news, name='blog'), 
    url(r'^comments/',views_comment.comments, name='comments'),
   # url(r'^galery/$', photo_list, name='photo_list'),
   # url(r'^galery/(?P<slug>[\w-]+)/$', show_photo, name='show_photo'),
    url(r'^galery/', include('galery.urls')),
    url(r'^contact/', views_contact.contact, name='contact'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^projects/view/(\d+)/', views.project_detail, name='project_detail'),
    url(r'^video/$', ListView.as_view(
    model=Video,
    context_object_name='videos',
    template_name='video.html'),
    name='video'
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
