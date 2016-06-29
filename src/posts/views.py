from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect

from .forms import PostForm

from .models import Post
# Create your views here.

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
		"form":form,
	}
	return render(request,"post_form.html",context)

def post_detail(request,id):
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id=id)
	context = {
			"title" : instance.title,
			"instance": instance
		}
	return render(request,"post_detail.html",context)
	#return HttpResponse("<h1>Detail</h1>")

def post_list(request):

	queryset=Post.objects.all()
	context={
		"object_list":queryset,
		"title" :"List"

	}
	'''if request.user.is_authenticated():
		context = {
			"title" : "My user List"
		}
	else:

		context = {
			"title" : "detail"
		}'''
	return render(request,"post_list.html",context)
	#return HttpResponse("<h1>List</h1>")

def post_update(request,id=None):

	instance = get_object_or_404(Post, id=id) 
	form = PostForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"<a href='#'> Item </a> saved", extra_tags='html_safe')

		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			"title" : instance.title,
			"instance": instance,
			"form":form,
		}
	return render(request,"post_form.html",context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id) 
	instance.delete()
	messages.success(request,"Successfully deleted")

	return redirect("posts:list")