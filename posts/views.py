
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy

from posts.models import Posts, Comments, Author, Category
from .forms import PostForm



class PostListView(ListView):
	model = Posts
	template_name = 'posts_list.html'

	def get_context_data(self, **kwargs):
		categories = Category.objects.all()
		latest = Posts.objects.order_by('-timestamp')[0:3]
		context = super().get_context_data(**kwargs)
		context['categories'] = categories
		context['latest'] = latest
		return context
        


class PostDetailView(DetailView):
	model = Posts
	template_name = 'posts_detail.html'
	
	


	def get_context_data(self, **kwargs):
		post = self.get_object()
		comments = Comments.objects.filter(post=post)
		categories = Category.objects.all()
		latest = Posts.objects.order_by('-timestamp')[0:3]
		kwargs['comments'] = comments
		kwargs['categories'] = categories
		kwargs['latest'] = latest

		return super().get_context_data(**kwargs)

	
@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
	model = Posts
	template_name = 'posts_form.html'
	fields = ['title', 'text', 'categories']

	def form_valid(self, form):
		post = form.save(commit=False)
		usr = get_object_or_404(Author, user=self.request.user)
		print (usr)
		post.author = usr
		post.save()
		return redirect('posts:post-list')






class PostUpdateView(UpdateView):
	model = Posts
	template_name = 'posts_form.html'
	fields = ['title', 'text','author', 'categories']	



class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'posts_confirm_delete.html'	
    success_url = ('/posts/')



def trial(request):			
	return render (request, "index.html")



@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
	model = Comments
	template_name = 'comment_form.html'
	fields = ['textarea']


	def form_valid(self, form):
		post = Posts.objects.get(pk=self.kwargs['pk'])
		athr = Author.objects.get(user=self.request.user)
		comment = form.save(commit=False)
		comment.created_by = athr
		comment.post = post
		comment.save()
		return redirect('posts:post-detail', self.kwargs['pk'])
	
	# def get_success_url(self):
	# 	return reverse ('posts:post-detail', kwargs={'pk':self.kwargs['pk']})




class CategoryDetailView(DetailView):
	model = Category
	template_name = 'category_detail.html'

	def get_context_data(self, **kwargs):
		cat = self.get_object()
		posts = Posts.objects.filter(categories=cat)
		kwargs['posts'] = posts
		return super().get_context_data(**kwargs)
