from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy





class Category(models.Model):
	title = models.CharField(max_length=20)

	class Meta:
		verbose_name_plural='Categories'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse ('posts:category-detail', kwargs={'pk':self.pk})
		



class Author(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username


class Posts(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	categories = models.ManyToManyField(Category)

	class Meta:
		verbose_name_plural="Posts"

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('posts:post-detail', kwargs={'pk':self.pk})

	def get_update_url(self):
		return reverse('post-update', kwargs={'pk':self.pk})

	def get_delete_url(self):
		return reverse('post-delete', kwargs={'pk':self.pk})






class Comments(models.Model):

	textarea = models.TextField()
	created_by = models.ForeignKey(Author, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Posts, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural='Comments'

	def __str__(self):
		return self.textarea

	def get_absolute_url(self):
		return reverse('posts:post-comment', kwargs={'pk':self.pk})
	



	
	






		

	

	
        
