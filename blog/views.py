from django.shortcuts import render
from django.utils import timezone
# The dot before models means current directory or current application
# both views.py and models.py are in the same directory. This means we can use . and the name of the file (without .py)
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# returns a function 'render' that will render(put together) the template 'blog/post_list.html'
	# request: a parameter, everything we receive from the user via the Internet 
	# the last parameter {}, is a place in which we can add some things for the template to use
	return render(request, 'blog/post_list.html',{'posts':posts})
