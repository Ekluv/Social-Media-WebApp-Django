from django import forms
from django.contrib.auth.models import User

from .models import Post,Like


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title']

	def clean_title(self):
		title = self.cleaned_data.get('title')
		return title

class LikeForm(forms.ModelForm):
	class Meta:
		model = Like
		fields = ['voter','post']
		exclude = ['voter','post']