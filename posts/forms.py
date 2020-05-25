from django.forms import ModelForm


from .models import Posts, Comments

class PostForm(ModelForm):

	class Meta:
		model = Posts
		fields = "__all__"

class CommentForm(ModelForm):

	class Meta:
		model = Comments
		fields = ['textarea']		
