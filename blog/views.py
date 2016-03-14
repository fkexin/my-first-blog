from django.shortcuts import render

# Create your views here.
def post_list(request):
	# returns a function 'render' that will render(put together) the template 'blog/post_list.html'
	return render(request, 'blog/post_list.html',{})
