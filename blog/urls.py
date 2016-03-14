from django.conf.urls import url
# import all of our views from blog application
from . import views

urlpatterns = [
	# assigning a 'view' called 'post_list' to '^$' URL. 
	# this regex will match '^' at the beginning followed by '$' at the end
	# so only an empty string will match
	# in Django URL resolvers, 'http://127.0.0.1:8000/' is NOT a part of the URL
	# This pattern tells that 'views.post_list' is the right place to go if 
	# someone enters 'http://127.0.0.1:8000/'

	# name ='post_list'   is the name of the URL that will be used to identify the view
	# it can be the same as the name of the view, but it can also be different
	# name each URL and be unique

	url(r'^$', views.post_list, name = 'post_list'),
]