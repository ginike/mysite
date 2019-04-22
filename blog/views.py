from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
import operator
from .forms import PostForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


from django.views.generic import (ListView,
 DetailView,
 UpdateView,
 DeleteView, 
  CreateView
  )


#Creating a function base home view
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

#Creating a Class Based View
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'#override
	context_object_name = 'posts'#overide
	ordering = ['-date_posted']#sorting accordint to the latest date
	paginate_by = 5

	


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'#override
	context_object_name = 'posts'#overide
	#ordering = ['-date_posted']#sorting accordint to the latest date
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


#using the default generic view 
class PostDetailView(DetailView):
	model = Post

@method_decorator(staff_member_required, name='dispatch')
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'composer', 'genre', 'doc_file', 'new_price', 'sample_view']
	#checking if the one creating is logged in/or is a user
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
@method_decorator(staff_member_required, name='dispatch')
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'composer', 'doc_file','sample_view']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

#checking if the author is the one updating
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

#checking if the author is the one updating
@method_decorator(staff_member_required, name='dispatch')
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



def about(request):
	return render(request, 'blog/about.html', {'title':'About'})

#def first_page(request):
#	return render(request, 'blog/index.html')


def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(composer__icontains=query)

            results= Post.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'blog/home.html', context)

        else:
            return render(request, 'blog/home.html')

    else:
        return render(request, 'blog/home.html')




def search_by_anthem(request):	
	
	context={
		'posts':Post.objects.filter(genre='Anthem')
	}
	print (context)
	return render(request, 'blog/anthems.html', context) 


def search_by_classical(request):	

	context={
		'posts':Post.objects.filter(genre='Classical')
	}
	print (context)
	return render(request, 'blog/classicals.html', context) 



def search_by_highlife(request):	

	context={
		'posts':Post.objects.filter(genre='Highlife')
}
	print (context)
	return render(request, 'blog/highlife.html', context) 


def search_by_hymn(request):	

	context={
		'posts':Post.objects.filter(genre='Hymn')
}
	print (context)
	return render(request, 'blog/hymns.html', context) 
#else:
#	return render(request, 'blog/home.html') 

class PostUpView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = []
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def plans(request):
	return render(request, 'blog/plans.html')

#from django.contrib.admin.views.decorators import staff_member_required
#from django.utils.decorators import method_decorator


#@method_decorator(staff_member_required, name='dispatch')
#class ExampleTemplateView(TemplateView):
 #   ...

