from django import forms
from .models import Post


class PostForm(forms.ModelForm):

	class Meta:
		# use Post model to create this form 
		model = Post
		# only the title and text to be exposed
		fields = ('title','text',)
		