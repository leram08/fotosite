from django.shortcuts import render
from .models import *
from comment.forms import *

def comments(request):
	recent_comments = Comment.objects.filter(check=True).order_by('-date')
	#context = {'comments': recent_comments,}
	if request.method == 'POST':
		#import pdb; pdb.set_trace()
		form = CommentForm(request.POST,request.FILES)
		if form.is_valid():
			load=True
			import pdb; pdb.set_trace()
			comments = Comment(name=form.cleaned_data['name'], email=form.cleaned_data['email'],message=form.cleaned_data['message'],photo=request.FILES['photo'])
			#import pdb; pdb.set_trace()
			comments.save()
			form=CommentForm()
		else:
			load=False
	else:
		load=True
		form = CommentForm()
	return render(request, 'comments.html', {'comments':recent_comments,'form':form,'load':load})