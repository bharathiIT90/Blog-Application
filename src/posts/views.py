from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request):
	context = {
			"title" : "detail"
		}
	return render(request,"index.html",context)
	#return HttpResponse("<h1>Detail</h1>")

def post_list(request):
	if request.user.is_authenticated():
		context = {
			"title" : "My user List"
		}
	else:

		context = {
			"title" : "detail"
		}
	return render(request,"index.html",context)
	#return HttpResponse("<h1>List</h1>")

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")