from django.db import models
from django.utils import timezone

# Create your models here.
# defines the model(an object), 'Post' is the name of the model. 
# **always start a class name with an upperclass letter**
# models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database
class Post(models.Model):
	# now define the Properties: author, title, text, etc
	# need to define a Type of each field
	# models.ForeignKey - a link to another model
	author = models.ForeignKey('auth.User')
	# models.CharField - define a text with a limited number of characters
	title = models.CharField(max_length=200)
	# models.TextField - for long text without a limit
	text = models.TextField()
	# models.DateTimeField - date and time
	Create_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)
 
	# define Methods, indented inside the class
	# def means that this is a Function/Method 
	# publish is the name
	# naming rule: lowercase letters and underscores
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

