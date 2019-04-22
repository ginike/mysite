from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'composer', 'doc_file','sample_view', 'new_price','date_posted', 'genre')



