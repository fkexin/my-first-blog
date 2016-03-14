from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
# The dot before models means current directory or current application
# both views.py and models.py are in the same directory. This means we can use . and the name of the file (without .py)
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# returns a function 'render' that will render(put together) the template 'blog/post_list.html'
	# request: a parameter, everything we receive from the user via the Internet 
	# the last parameter {}, is a place in which we can add some things for the template to use
	return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request,'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		# open a form with this post to edit
		form = PostForm(instance=post)
	return render(request,'blog/post_edit.html',{'form':form})
