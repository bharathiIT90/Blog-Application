from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Post
# Create your views here.

def post_create(request):
	return HttpResponse("<h1>Create</h1>")

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
	return render(request,"index.html",context)
	#return HttpResponse("<h1>List</h1>")

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")