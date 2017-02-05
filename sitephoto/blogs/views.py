from django.shortcuts import render
from .models import *
# Create your views here

def news(request):
    recent_blogs = Blogs.objects.all().order_by('-publish_date')
    context = {'blogs': recent_blogs,}
    #import pdb; pdb.set_trace()
    return render(request, 'blog.html', context)


def project_detail(request, project_id):
    project_object = Blogs.objects.filter(id=project_id)
    project_object = project_object[0] 
    #import pdb; pdb.set_trace()
    context = {
        'project': project_object,
    }
    return render(request, 'project_detail.html', context)